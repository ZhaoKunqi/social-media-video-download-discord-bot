import discord
import yt_dlp
import os

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
            'outtmpl': '/root/discord/bot/downloads/%(uploader_id)s-%(id)s.%(ext)s',
            'cookiefile': '/root/discord/bot/cookies-twitter.txt'
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(message.content, download=True)
            filename = ydl.prepare_filename(info_dict)

        s3_filename = os.path.basename(filename)
        os.system(f's3cmd put {filename} s3://Your-Bucket-Name/{s3_filename} --acl-public')

        reply_message = f"""Original Address:\n```{message.content}```\nObject Storage Address:\n```https://Your-S3-Address/Your-Bucket-Name/{s3_filename}```"""
        await message.channel.send(reply_message, file=discord.File(f'/root/discord/Quincy0v0/downloads/{s3_filename}'))

        os.remove(filename)



client.run('Your-Discord-App-Token')
