from os.path import isfile

from flask import Blueprint, Response, abort

from ..config import STATIC_BPNAME, CURRENT_PATH

static = Blueprint(STATIC_BPNAME, __name__)

@static.route("/css/<path:file_name>")
def css(file_name=''):
    if file_name.endswith('.map'):
        if isfile(f'{CURRENT_PATH}/static/css/{file_name}'):
            with open(f'{CURRENT_PATH}/static/css/{file_name}',"rb")as file:
                css_text = file.read()
        else:
            file_name=''
            abort(404)
    else:
        if isfile(f'{CURRENT_PATH}/static/css/{file_name}.css'):
            with open(f'{CURRENT_PATH}/static/css/{file_name}.css',"rb")as file:
                css_text = file.read()
        else:
            file_name=''
            abort(404)
    file_name = ''
    return Response(css_text, mimetype='text/css')

@static.route("/image")
def images():
    file_name = f'{CURRENT_PATH}/static/images/2.svg'
    mimetype = 'image/svg+xml'
    with open(file_name,"rb")as file:
        image = file.read()
    response = Response(mimetype=mimetype)
    response.set_data(image)
    return response
