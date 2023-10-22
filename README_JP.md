# Discord Twitter 動画ダウンロードボット

[中文(中华人民共和国)文档](README.md) | [English Document](README_US.md) | [日本語文档(現在のページ)]

このプロジェクトは、Discord ボットで、Twitter(x.com)のリンクが含まれたDMから動画を自動的にダウンロードすることができます。 

`yt-dlp`を使用しています。これは、Pythonライブラリとコマンドラインプログラムで、x.comからビデオをダウンロードするために使用されます。

ダウンロードが完了すると、ファイルをS3ストレージバケットにアップロードし、元のTwitterリンクと新しいS3リンクのメッセージをDMで送信します。 このメッセージには、ビデオファイルも添付ファイルとして含まれています。

## 機能

- Discordのメッセージ内のTwitterリンクを検出し、関連する動画を自動的にダウンロードする
- ダウンロードした動画をS3ストレージバケットにアップロードする
- 元のTwitterリンク、S3リンク、ビデオファイル添付を含むメッセージをDiscordのDMで送信する

## 直接使用

現在、S3バックアップ機能のないパブリックボットを提供しています。無料で使用できます。現在の頻度制限は、各Discordアカウント/1時間あたり60本の動画です。

ボットリンク(権限不要): https://discord.com/api/oauth2/authorize?client_id=1153911158730928128&permissions=0&scope=bot

ボットをサーバーに招待し、Twitter(x.com)のリンクを含むDMを送信するだけで使用できます。

## 自身でのデプロイ(systemd方式)

RHELベースのLinuxディストリビューションでのインストールと使用方法。

ここではAlma Linux 9を使用しています。

### 前提条件

- Python 3.6以上
- Discord APIトークン
- S3 API互換のブロックストレージ(なければ、configでs3-backupをfalseに設定する)

### 手順

1. 必要なRPMパッケージをインストール:
   ```
   dnf install git python python-pip -y
   ```

2. プロジェクトをクローン:
   ```
   git clone https://github.com/ZhaoKunqi/social-media-video-download-discord-bot.git
   ```

3. プロジェクトディレクトリに移動:
   ```
   cd social-media-video-download-discord-bot
   ```

4. 必要なPythonパッケージをインストール:
   ```
   pip install -r requirements.txt
   ```
       
5. 設定

  ボットを使用するには、config.ymlファイルを変更する必要があります。
  
- `discord-bot-token`: Discordボットのトークン
- `cache-directory`: 動画のキャッシュディレクトリ
- `cache-clean`: DiscordとS3(有効な場合)へのアップロード後に動画キャッシュを削除するかどうか  
- `x-cookie`: x.comのクッキーファイルを指定
- `enable-s3-backup`: S3バックアップを有効にするかどうか。falseの場合、他のS3設定は無視される
- `s3-endpoint`: S3 APIサーバーのアドレス
- `s3-access-front-end`: S3フロントエンドアドレス。ユーザーに送信されるメッセージに表示される
- `s3-access-key` と `s3-secret-key`: S3サーバー認証に使用するキー
- `s3-bucket-name`: バケット名(事前に作成しておき、アクセス権限が必要)
- `s3-upload-timeout`: S3アップロードのタイムアウト制限(秒)

7. ボットの実行:
   ```
   python3 main.py
   ```

8. systemdサービスとして実行

   ```
   cp discord-bot.service /etc/systemd/system/
   # ディレクトリを変更する必要がある場合は vim で編集
   vim /etc/systemd/system/discord-bot.service
   
   systemctl daemon-reload
   systemctl enable /etc/systemd/system/discord-bot.service --now
   ```

## 例

![example01.jpg](example01.jpg)

## 更新歴

2023年9月26日: S3同期機能を最適化し、タイムアウト機能を追加。config.yamlに新しい設定`s3-upload-timeout`を追加。S3サーバーへの接続が上手くいかない場合でもユーザーに動画を返せるようになり、安定性が向上しました。

2023年9月20日: 設定ファイルのフォーマットを改善し、よりカスタマイズできるオプションを追加、ドキュメントを更新

2023年9月10日: 現在、x.com(Twitter)のアプリがリンクをコピーすると自動的にx.comリンクを生成するようになったため、x.comリンク内の動画も認識するように変更しました。

## 貢献

このプロジェクトに貢献したい場合は、いつでもリポジトリをフォークしてプルリクエストを送信してください。また、発生した問題も歓迎します。

## ライセンス

このプロジェクトはMITライセンスです。詳細はLICENSEファイルを参照してください。
