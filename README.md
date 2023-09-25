# Discord Twitter 视频下载机器人


[中文(中华人民共和国)文档(当前页面)] | [English Document](README_ENUS.md)

该项目是一个 Discord 机器人，可以自动从私信中接收的 Twitter(x.com) 链接下载视频。

它使用 `yt-dlp`，一个用于从 x.com 下载视频的 Python 库和命令行程序，从 Twitter 链接中获取视频。

下载完成后，它会将文件上传到 S3 存储桶，并通过私信向您发送原始的 Twitter 链接和新的 S3 链接的消息。该消息还包含视频文件作为附件。

## 功能

- 检测 Discord 消息中的 Twitter 链接，并自动下载关联的视频。
- 将下载的视频上传到 S3 存储桶。
- 通过 Discord 私信发送包含原始的 Twitter 链接、S3 链接和视频文件附件的消息。

## 直接使用

目前提供一个不带S3备份功能的Bot, 可以免费使用, 当前频率限制为: 每个Discord账号/60个视频/每小时

机器人链接(无需权限): https://discord.com/api/oauth2/authorize?client_id=1153911158730928128&permissions=0&scope=bot

随便加进来私聊发给他推特链接(x.com的)即可使用

## 自己部署

在 RHEL-based Linux 发行版上的安装和使用

这里使用Alma Linux 9

### 前置条件

- Python 3.6 或更高版本
- Discord API 令牌
- 兼容 S3 API 的块存储(如果没有，则要在配置文件里将enable-s3-backup设置为False)

### 步骤

1. 安装所需的 RPM 软件包：
   ```
   dnf install git python python-pip -y
   ```

2. 克隆项目：
   ```
   git clone https://github.com/ZhaoKunqi/social-media-video-download-discord-bot.git
   ```

3. 进入项目目录：
   ```
   cd social-media-video-download-discord-bot
   ```

4. 安装所需的 Python 包：
   ```
   pip install -r requirements.txt
   ```
   
5. 配置

  要使用该机器人，您需要对 config.yml 文件进行一些更改。

- `discord-bot-token`：您的 Discord 机器人使用的令牌
- `cache-directory`：缓存视频的目录
- `cache-clean`：在上传到 Discord 和 S3（如果启用）之后是否删除视频缓存
- `x-cookie`：指定 X.com 的 cookie 文件
- `enable-s3-backup`：是否启用 S3 备份。如果为 false，则其他 S3 配置将不会生效
- `s3-endpoint`：S3 API 服务器地址
- `s3-access-front-end`：S3前端地址,会出现在发送给用户的消息中
- `s3-access-key` 和 `s3-secret-key`：S3 服务器验证的密钥
- `s3-bucket-name`：Bucket 名称（必须提前创建好，并且您需要有访问权限）
- `s3-upload-timeout`：S3上传超时限制(秒)

7. 运行机器人：
   ```
   python3 main.py
   ```

8. 使用systemd托管作为服务来运行

   ```
   cp discord-bot.service /etc/systemd/system/
   # 您需要修改对应的目录
   vim /etc/systemd/system/discord-bot.service

   systemctl daemon-reload
   systemctl enable /etc/systemd/system/discord-bot.service --now
   ```

## 效果预览

![example01.jpg](example01.jpg)

## 更新记录:

2023年-09月-20日: 改进配置文件格式，添加更多自定义选项，更新文档

2023年-09月-10日: 因为现在X.com(Twitter)的App更改成会在分享复制链接时自动生成x.com的链接，所以也改成了识别x.com链接中视频。

## 贡献

如果您想为该项目做出贡献，请随时 fork 该存储库并提交拉取请求。我们也欢迎您遇到的任何问题。

## 许可证

本项目采用 MIT 许可证。有关详细信息，请参阅 LICENSE 文件。
