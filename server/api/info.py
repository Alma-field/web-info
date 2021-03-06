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
        ip_address = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
        ip_fowarded = request.environ.get('HTTP_X_FORWARDED_FOR', None)
        if ip_fowarded is not None:
            ip_address = ip_fowarded
        data = {
            'code': 200,
            'type': 'ipaddress',
            'value': ip_address
        }
        return data

@api.route(
    '/useragent',
    doc={'description': 'クライアントのユーザーエージェントを返却します。'}
)
class UserAgent(Resource):
    """UserAgent"""

    @api.marshal_with(data)
    def get(self):
        user_agent = request.headers['User-Agent']
        data = {
            'code': 200,
            'type': 'user-agent',
            'value': user_agent
        }
        return data

def main():
    pass
