# Key Management
![license](https://img.shields.io/badge/license-MIT-blue.svg)
[![GitHub issues open](https://img.shields.io/github/issues/Alma-field/web-info.svg?maxAge=2592000)](https://github.com/Alma-field/web-info/issues?q=is%3Aopen+is%3Aissue)
[![GitHub issues close](https://img.shields.io/github/issues-closed-raw/Alma-field/web-info.svg?maxAge=2592000)](https://github.com/Alma-field/web-info/issues?q=is%3Aclose+is%3Aissue)

これはブラウザー情報システムです。

## 目次
 - [使用方法](#使用方法)
   - [ローカルでテストを行う場合](#ローカルで実行する場合)
   - [Herokuでテストを行う場合](#Herokuで実行する場合)
 - [実行時パラメータ](#実行時パラメータ)

## 使用方法

### ローカルで実行する場合
1. このリポジトリをローカル環境に複製してください。
```shell
git clone -b flask https://github.com/Alma-field/web-info
```
2. `pip install -r requirements.txt`を実行しライブラリをダウンロードします。
3. `python main.py  [--host <host>] [--port <port>]`を実行してください。
4. エンドポイントURL（`https://localhost[:<port>]`）にWebブラウザーからアクセスし、アプリが正しく動作していることを確かめてください。<br>正しく動作していれば、 トップページが表示されます。

### Herokuで実行する場合
__[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Alma-field/web-info)__
1. 上記の**Deploy to Heroku** ボタンをクリックします。
2. Herokuの「Create New App」ページで、必要事項を入力します。
3. **Deploy app**をクリックします。
4. **View**をクリックしてアプリのデプロイが成功したことを確認します。<br>「You have not assigned any value for EMAIL_ADDRESS and EMAIL_PASSWORD」のメッセージが画面に表示されていたらデプロイができています。
5. エンドポイントURL（`https://{Herokuアプリ名}.herokuapp.com`）にWebブラウザーからアクセスし、アプリが正しく動作していることを確かめてください。<br>正しく動作していれば、 トップページが表示されます。

## 実行時パラメータ
| 項目 | 説明 |
| :--: | -- |
| -H<br>--host | ホスト名<br>LANに公開しない場合は`localhost`を指定してください<br>(デフォルト: `0.0.0.0`) |
| -p<br>--port | ポート番号<br>(デフォルト: `5000`) |
| -d | Flaskをデバッグモードで起動します。<br>(フラグパラメータ) |

 - 例：`python main.py -H localhost -p 8000 -d`
