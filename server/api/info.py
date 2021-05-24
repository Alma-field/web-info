from flask import request, abort
from flask_restx import Resource

#from .. import app

from . import api

from .models.data import data

@api.route(
    '/ipaddress',
    doc={'description': 'クライアントのIPアドレスを返却します。'}
)
class IPAddress(Resource):
    """IPAddress"""

    @api.marshal_with(data)
    def get(self):
        ipaddress = request.remote_addr
        data = {
            'code': 200,
            'type': 'ipaddress',
            'value': ipaddress
        }
        return data

def main():
    pass
