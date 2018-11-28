# wsgi.py
from flask import Flask
from flask import jsonify
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/api/v1/products')
def get_products():
    PRODUCTS = [
        {'id': 1, 'name': 'Skello'},
        {'id': 2, 'name': 'Socialive.tv'},
        {'id': 3, 'name': 'toto'}
    ]

    return jsonify(PRODUCTS)
