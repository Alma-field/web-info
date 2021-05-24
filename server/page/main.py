from datetime import datetime

from flask import request, make_response, render_template

from .. import app

from ..config import CURRENT_PATH, TIMEZONE

@app.route('/')
def root_page():
    data = {}
    data['date'] = [
        '取得時刻',
        datetime.now(TIMEZONE).strftime('%Y年%m月%d日 %H時%M分%S秒')
    ]
    data['ipaddress'] = ['IPアドレス', request.remote_addr]
    data['form-type'] = ['FORMタイプ', request.method.upper()]
    data['user-agent'] = ['ブラウザー', request.headers['User-Agent']]
    data['accept-mime'] = ['使用するMIME', request.headers['Accept']]
    data['accept-encoding'] = ['使用するエンコード', request.headers['Accept-Encoding']]
    data['accept-lang'] = ['使用言語', request.headers['Accept-Language']]
    response = make_response(render_template('root_page.html', data=data))
    return response

@app.route('/robots.txt')
def show_robotstxt():
    with open(f'{CURRENT_PATH}/static/robots.txt', "r", encoding='utf-8') as file:
        text = file.read()
    return text

def main():
    pass
