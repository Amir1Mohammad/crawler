# Python imports
import datetime
import jwt
# Flask imports
from flask import jsonify, request, make_response

# Project imports
from controller import app

__Author__ = "Amir Mohammad"


@app.route('/api_1/get_token', methods=['POST'])
def authorization():


    auth = request.authorization
    print(auth)
    if auth and auth.username == 'Amir' and auth.password == '09128020911':
        token = jwt.encode({'user': auth.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
                           app.config['SECRET_KEY'])
        return jsonify({'token': token.decode('UTF-8')})

    return make_response({'message': 'Could not verify token'}, 401, {'WWW-Authenticate': 'Basic real="Login Required"'})
