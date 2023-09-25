# Discord Twitter Video Download Bot

[English Document (Current Page)] | [中文(中华人民共和国)文档](README.md) 

This project is a Discord bot that can automatically download videos from Twitter (x.com) links sent to it in DMs.

It uses `yt-dlp`, a Python library and command-line program for downloading videos from x.com, to fetch videos from Twitter links. 

After downloading, it will upload the files to an S3 bucket, and DM you back with the original Twitter link, new S3 link, and the video file as an attachment.

## Features

- Detects Twitter links in Discord messages and automatically downloads associated videos
- Uploads downloaded videos to an S3 bucket
- Sends back a DM with original Twitter link, S3 link, and video file attachment

## Use Ready Bot Directly

Currently there is a public bot available to use for free, with rate limiting to 60 videos per hour per Discord account:

Bot invite link (no permission needed): https://discord.com/api/oauth2/authorize?client_id=1153911158730928128&permissions=0&scope=bot

Just add it to any server and DM it x.com (Twitter) links.

## Self-Hosting

Installation and usage on RHEL-based Linux distros

Here we use Alma Linux 9 as an example

### Prerequisites

- Python 3.6 or higher
- Discord API token 
- S3-compatible object storage if you want S3 backup (otherwise set enable-s3-backup to false in config)

### Steps 

1. Install required RPM packages:
   ```
   dnf install git python python-pip -y
   ```

2. Clone the project:
   ```
   git clone https://github.com/ZhaoKunqi/social-media-video-download-discord-bot.git
   ```

3. Enter the project directory:
   ```
   cd social-media-video-download-discord-bot
   ```

4. Install required Python packages:
   ```
   pip install -r requirements.txt
   ```
   
5. Configure the config.yml file:

  To use this bot, you'll need to modify some things in config.yml:

- `discord-bot-token`: Token your Discord bot uses 
- `cache-directory`: Directory to cache downloaded videos
- `cache-clean`: Whether to delete video cache after uploading to Discord and S3 (if enabled)
- `x-cookie`: Specify x.com cookie file
- `enable-s3-backup`: Whether to enable S3 backup. Other S3 configs will not apply if this is false.
- `s3-endpoint`: S3 API server address  
- `s3-access-front-end`: S3 frontend address to include in messages to user
- `s3-access-key` and `s3-secret-key`: Keys for authenticating with S3 server
- `s3-bucket-name`: Bucket name (must exist ahead of time and you must have access)
- `s3-upload-timeout`: S3 upload timeout limit in seconds

7. Run the bot:
   ```
   python3 main.py
   ```
   
8. Use systemd to run it as a service:

   ```
   cp discord-bot.service /etc/systemd/system/
   # Modify paths as needed
   vim /etc/systemd/system/discord-bot.service
   
   systemctl daemon-reload
   systemctl enable /etc/systemd/system/discord-bot.service --now
   ```

## Preview

![example01.jpg](example01.jpg)

## Changelog:

Sep 20, 2023: Improved config file format, added more customization options, updated docs

Sep 10, 2023: Added support for x.com links as Twitter app now autogenerates those when sharing copy link

## Contributing

Feel free to fork this repo and submit pull requests if you would like to contribute. We also welcome any issues you encounter.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
