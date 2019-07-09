# Flask imports
from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES

__Author__ = "Amir Mohammad"


def bad_request(message):
    return error_response(400, message)


def unauthorized(message):
    return error_response(401, message)


def not_found():
    pass


def server_error():
    pass


def error_response(status_code, message=None):
    payload = {'error': HTTP_STATUS_CODES.get(status_code, 'Unknown error')}
    if message:
        payload['message'] = message
    response = jsonify(payload)
    response.status_code = status_code
    return response
