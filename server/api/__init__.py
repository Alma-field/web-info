from flask_restx import Api

from .. import app

api = Api(
    app,
    version='1.0.0',
    title='Key Management API',
    description='Web情報API',
    base_url='alma-field-vpn.tplinkdns.com',
    base_path='/'
)

from .error import main

from .info import main
