# wsgi.py
from flask import Flask
from flask import jsonify
from flask import abort
app = Flask(__name__)

PRODUCTS = [
    {'id': 1, 'name': 'Skello'},
    {'id': 2, 'name': 'Socialive.tv'},
    {'id': 3, 'name': 'toto'}
]

@app.route('/')
def hello():
    return "Hello World!"


@app.route('/api/v1/products')
def get_products():
    return jsonify(PRODUCTS)


@app.route('/api/v1/products/<int:id>')
def get_product(id):
    for product in PRODUCTS:
        if product['id'] == id:
            return jsonify(product)

    return abort(404)





