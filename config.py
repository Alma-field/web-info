# .env ファイルをロードして環境変数へ反映
from os import environ
from dotenv import load_dotenv

JSON_AS_ASCII = False

load_dotenv('./.env', encoding='utf-8')
PORT = int(environ.get("PORT", 5000))
