from datetime import datetime

from flask import Markup

from .. import app

###################カスタムフィルター
@app.template_filter('linebreaksbr')
def linebreaksbr(arg):
    return Markup('<br>\n'.join(str(arg).splitlines()))

@app.template_filter('hexstring')
def linebreaksbr(arg):
    return Markup('{:016X}'.format(arg)[-16:])

@app.template_filter('halfmask')
def halfmask(arg):
    length = int(len(arg) / 2)
    return Markup(arg[:length]+''.join(['*']*length))

@app.template_filter('stringmask')
def stringmask(arg):
    return Markup(''.join(['*']*len(arg)))

@app.template_filter('jssafe')
def jssafe(arg):
    return Markup(arg.replace('True', 'true').replace('False', 'false'))

@app.template_filter('comma')
def comma(arg):
    try:
        return Markup(f'{int(arg):,}')
    except:
        return Markup(arg)

def main():
    pass
