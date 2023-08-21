# Discord Twitter Video Downloader Bot

This project is a Discord bot that automatically downloads videos from Twitter links received from DM. It uses `yt-dlp`, a python library and command-line program to download videos from Twitter.com, to fetch the video from the Twitter link. After downloading the video, it uploads the file to an S3 bucket and then sends a message to your DM with the original Twitter link and the new S3 link. It also includes the video file as an attachment in the message. 

## Features

- Detects Twitter links in Discord messages and automatically downloads the associated video.
- Uploads the downloaded video to an S3 bucket.
- Sends a message to the Discord DM with the original Twitter link, the S3 link, and the video file as an attachment.

## Installation & Usage on RHEL-based Linux distros(Alma Linux 9)

### Prerequisites

- Python 3.6 or higher
- Discord API Token
- S3-API compatible block storage
- `s3cmd` installed

### Steps

1. Install required RPM packages:
   ```
   dnf install git python python-pip s3cmd -y
   ```

2. Clone the project:
   ```
   git clone https://github.com/ZhaoKunqi/social-media-video-download-discord-bot.git
   ```
3. Navigate to the project directory:
   ```
   cd social-media-video-download-discord-bot
   ```
4. Install the required python packages:
   ```
   pip install -r requirements.txt
   ```

5. Configure the s3cmd:
   ```
   #use interactive configuration method
   s3cmd --configure
   #or edit config file manually
   vim /root/.s3cfg
   ```

   Careful:
   ```
   host_base = {{Fill your S3 API address here}}
   host_bucket = {{Leave here empty, Domain based S3 API is not recommend here unless you know what you doing}}
   ```


6. Open `main.py` in your preferred text editor and replace the following placeholders with your own information:
   - `'Your-Discord-App-Token'` with your Discord bot token.
   - `'Your-Bucket-Name'` with the name of your S3 bucket.
   - `'Your-S3-Address'` with the address of your S3 bucket.
   - `'cookies-twitter.txt'` with the path to your Twitter cookies file. This is necessary for `yt-dlp` to be able to download videos from Twitter.
   - `'/root/discord/bot/downloads/'` with the path where you want to store the downloaded videos.
7. Run the bot:
   ```
   python main.py
   ```

## Configuration

To use this bot, you will need to make some changes to the `main.py` file:

- Replace `'Your-Discord-App-Token'` with your Discord bot token.
- Replace `'Your-Bucket-Name'` and `'Your-S3-Address'` with the name and address of your S3 bucket respectively.
- Replace `'/root/discord/bot/downloads/'` with the path where you want to cache the downloaded videos.
- Replace `'cookies-twitter.txt'` with the path to your Twitter cookies file. This is necessary for `yt-dlp` to be able to download videos from Twitter.

## Contribution

If you want to contribute to this project, please feel free to fork the repository and submit a pull request. We also welcome any issues you may encounter.

## License

This project is currently have no license or any plan for add license to it.
