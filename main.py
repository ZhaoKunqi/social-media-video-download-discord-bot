import time,multiprocessing,itertools,argparse,os
import discord
import yt_dlp
import boto3
import yaml

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--config', default='config.yml', help='Path to the configuration file')
args = parser.parse_args()

# Load configurations from the YAML file
with open(args.config, "r") as ymlfile:
    cfg = yaml.safe_load(ymlfile)

# Initialize boto3 client for S3
s3 = boto3.client('s3',endpoint_url=cfg['s3-endpoint'],aws_access_key_id=cfg['s3-access-key'],aws_secret_access_key=cfg['s3-secret-key'])

# Discord Bot parts
client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!'):
        return

    if 'x.com' in message.content:
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            'outtmpl': cfg['cache-directory'] + '/%(uploader_id)s-%(id)s.%(ext)s',
            'cookiefile': cfg['x-cookie']
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(message.content, download=True)
            filename = ydl.prepare_filename(info_dict)

        s3_filename = os.path.basename(filename)
        if cfg['enable-s3-backup']:
            # Upload file to S3
            uploader_subprocess = multiprocessing.Process(target=s3_backup, args=(filename, s3_filename), name='Upload_Process')
            uploader_subprocess.start()
            uploader_subprocess.join(timeout=cfg['s3-upload-timeout'])
            uploader_subprocess.terminate()
            if uploader_subprocess.exitcode is None:
                reply_message = f"""Original Address:\n```{message.content}```\nObject Storage Address:\n```S3 Video Uploading timeout !```"""
                await message.channel.send(reply_message, file=discord.File(cfg['cache-directory'] + '/' + s3_filename))
            if uploader_subprocess.exitcode == 0:
                reply_message = f"""Original Address:\n```{message.content}```\nObject Storage Address:\n```{cfg["s3-access-front-end"]}/{cfg["s3-bucket-name"]}/{s3_filename}```"""
                await message.channel.send(reply_message, file=discord.File(cfg['cache-directory'] + '/' + s3_filename))
        else:
            reply_message = f"""Original Address:\n```{message.content}```"""
            await message.channel.send(reply_message, file=discord.File(cfg['cache-directory'] + '/' + s3_filename))

        if cfg['cache-clean']:
            os.remove(filename)

def s3_backup(filename, s3_filename):
    with open(filename, 'rb') as data:
        s3.upload_fileobj(data, cfg['s3-bucket-name'], s3_filename, ExtraArgs={'ACL': 'public-read'})

client.run(cfg['discord-bot-token'])
