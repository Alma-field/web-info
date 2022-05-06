# ビルドコンテナ
FROM python:3.10.4-buster as builder

RUN mkdir /app
WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

# 実行コンテナ
FROM python:3.10.4-slim-buster

COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /usr/local/bin/gunicorn /usr/local/bin/gunicorn
COPY . /app
WORKDIR /app

ENV APP_NAME=web-info
ENV APP_VERSION=v0.0.0(dev)

CMD ["gunicorn", "main:app" , "--config", "gunconfig.py"]
