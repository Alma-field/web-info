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
    ipaddress = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    data['ipaddress'] = ['IPアドレス', ipaddress]
    data['form-type'] = ['FORMタイプ', request.method.upper()]
    data['user-agent'] = ['ブラウザー', request.headers['User-Agent']]
    accept_mime = str(request.headers['Accept'])
    #accept_mime = ';<br>'.join(accept_mime.split(';'))+';'
    data['accept-mime'] = ['使用するMIME', accept_mime]
    accept_encoding = str(request.headers['Accept-Encoding'])
    #accept_encoding = ';<br>'.join(accept_encoding.split(';'))+';'
    data['accept-encoding'] = ['使用するエンコード', accept_encoding]
    accept_lang = str(request.headers['Accept-Language'])
    #accept_lang = ';<br>'.join(accept_lang.split(';'))+';'
    data['accept-lang'] = ['使用言語', accept_lang]
    response = make_response(render_template('root_page.html', data=data))
    return response

@app.route('/robots.txt')
def show_robotstxt():
    with open(f'{CURRENT_PATH}/static/robots.txt', "r", encoding='utf-8') as file:
        text = file.read()
    return text

def main():
    pass
