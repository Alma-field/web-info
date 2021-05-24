from flask_restx import fields

from .. import api

data = api.model(
    'Data',
    {
        'code': fields.Integer(required=True, description='Response Status Code.'),
        'type': fields.String(required=True, description='Response Data type.'),
        'value': fields.String(required=True, description='Data Value.'),
    }
)
