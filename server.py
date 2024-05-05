from flask import Flask, request, jsonify
from time import time

import random, string

app = Flask(__name__)
tokens = {}

@app.route('/token/', methods=['GET'])
def get_token():
    if time() - tokens.get('last_request', 0) < 5:
        return jsonify({'error': 'Too many requests'}), 429

    token = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
    tokens[token] = {'timestamp': time(), 'last_request': time()}
    return jsonify({'token': token})

@app.route('/token/', methods=['POST'])
def check_token():
    token = request.json.get('token')
    if not token or token not in tokens:
        return jsonify({'status': 'failed'}), 400

    if time() - tokens[token]['timestamp'] > 30:
        del tokens[token]
        return jsonify({'status': 'failed'}), 400

    return jsonify({'status': 'status'})

if __name__ == '__main__':
    app.run(debug=True)