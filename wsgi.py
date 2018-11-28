# wsgi.py
from flask import Flask
from flask import jsonify
from flask import abort
from flask import request
from counter import Counter

app = Flask(__name__)

PRODUCTS = [
    {'id': 1, 'name': 'Skello'},
    {'id': 2, 'name': 'Socialive.tv'},
    {'id': 3, 'name': 'toto'}
]

@app.route('/')
def hello():
    return "Hello World!"


@app.route('/api/v1/products', methods=['GET', 'POST'])
def get_products():
    if request.method == 'GET':
        return jsonify(PRODUCTS)
    else:
        new_product = request.get_json()
        ID = Counter()
        new_id = ID.next()
        PRODUCTS.append({'id': new_id, 'name': new_product['name']})
        return jsonify(201)


@app.route('/api/v1/products/<int:id>', methods=['GET', 'DELETE'])
def get_product(id):
    if request.method == 'GET':
        for product in PRODUCTS:
            if product['id'] == id:
                return jsonify(product)
    else:
        for product in PRODUCTS:
            if product['id'] == id:
                PRODUCTS.remove(product)
                return jsonify(204)
    return abort(404)





