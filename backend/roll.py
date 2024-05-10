# backend/server.py

from flask import Flask, jsonify
from flask_cors import CORS  # Import CORS from flask_cors

app = Flask(__name__)
CORS(app)  

import random

@app.route('/', methods=['GET'])
def roll_dice():
    roll = random.randint(1, 6)
    return jsonify({'result': roll})

if __name__ == '__main__':
    app.run(debug=True)