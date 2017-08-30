import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../"))

from flask import Flask, request

import mocks.data
from services.services import SupermarketService, ProductService
from utils.core import catch_exception, return_json

app = Flask(__name__)


@app.route('/supermarkets')
@catch_exception()
def get_supermarkets():
    name = request.values.get('name', None)
    return return_json(SupermarketService.get_supermarkets(name))


@app.route('/products')
@catch_exception()
def get_products():
    name = request.values.get('name', None)
    return return_json(ProductService.get_products(name))


@app.route('/supermarkets/<name>/products')
@catch_exception()
def get_supermarket_products(name):
    return return_json(SupermarketService.get_supermarket_products(name))


if __name__ == '__main__':
    app.run()