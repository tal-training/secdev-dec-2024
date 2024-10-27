


from flask import Flask, jsonify, request, abort
import jwt
import datetime

app = Flask(__name__)
app.secret_key = 'your-secret-key'

def create_token(username):
    payload = {'sub': username}
    token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
    return token

@app.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        abort(400)
    username = request.json.get('username')
    token = create_token(username)
    return jsonify({'token': token})

@app.route('/protected', methods=['GET'])
def protected():
    token = request.headers.get('Authorization').split(' ')[1]
    try:
        token = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        abort(403)
    return jsonify({'message': 'Access granted', 'token': token})
