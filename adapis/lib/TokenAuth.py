from functools import wraps
from flask import request
import os

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'X-API-KEY'
    }
}

KEY = os.environ.get('TOKEN_KEY')

def token_required(f):
    @wraps(f)
    def decorated(*agrs, **kwagrs):

        token = None

        if 'X-API-KEY' in request.headers:
            token = request.headers['X-API-KEY']

        if not token:
            return {'message': 'Token is missing.'}, 401

        if token !=  KEY:
            return {'message': 'Your Token is Wrong or Invalid'}, 401

        # print('TOKEN: {}'.format(token) )
        return f(*agrs, **kwagrs)

    return decorated


def token_admin_required(f):
    @wraps(f)
    def decorated(*agrs, **kwagrs):

        token = None

        if 'X-API-KEY' in request.headers:
            token = request.headers['X-API-KEY']

        if not token:
            return {'message': 'Token is missing.'}, 401

        if token != 'admin3246':
            return {'message': 'Require Access Admin Token : Your Token is Wrong or Invalid'}, 401

        # print('TOKEN: {}'.format(token) )
        return f(*agrs, **kwagrs)

    return decorated
