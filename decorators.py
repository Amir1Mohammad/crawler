# Python imports
from functools import wraps
import jwt

# Flask imports
from flask import request
from flask import jsonify

# Project imports
from controller import app

__Author__ = "Amir Mohammad"


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')

        if not token:
            return jsonify({'message': 'token is missing'}), 403
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({'message': 'Token is invalid'}), 403
        return f(*args, **kwargs)

    return decorated
