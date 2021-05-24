import json
from flask import make_response, jsonify, abort
from werkzeug.exceptions import (
    BadRequest, Unauthorized, Forbidden, NotFound, MethodNotAllowed,
    InternalServerError, ServiceUnavailable
)

from .. import app

from ..config import CURRENT_PATH

from . import api

@app.errorhandler(400)
@app.errorhandler(401)
@app.errorhandler(403)
@app.errorhandler(404)
@app.errorhandler(405)
@app.errorhandler(500)
@app.errorhandler(503)
def error_handler(error):
    with open(f'{CURRENT_PATH}/templates/error.json', "r", encoding='utf-8')as file:
        errors = json.load(file)
    try:
        error_json = errors[str(error.code)]
    except:
        error_json = errors['500']
    response = make_response(jsonify(error_json), error_json['status_code'])
    return response

@api.errorhandler(BadRequest)
@api.errorhandler(Unauthorized)
@api.errorhandler(Forbidden)
@api.errorhandler(NotFound)
@api.errorhandler(MethodNotAllowed)
@api.errorhandler(InternalServerError)
@api.errorhandler(ServiceUnavailable)
def restx_handler(error):
    with open(f'{CURRENT_PATH}/templates/error.json', "r", encoding='utf-8')as file:
        errors = json.load(file)
    try:
        error_json = errors[str(error.code)]
    except:
        error_json = errors['500']
    response = make_response(jsonify(error_json), error_json['status_code'])
    return error_json, error_json['status_code']

@app.route("/error/<int:code>")
def error(auth, code):
    if code in [400, 401, 403, 404, 405, 500, 503]:
        abort(code)
    else:
        abort(404)

def main():
    pass
