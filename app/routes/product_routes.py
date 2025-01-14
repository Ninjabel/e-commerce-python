from flask import Blueprint, jsonify, request
from app.models.product import Product

product_bp = Blueprint('product', __name__)

@product_bp.route('/', methods=['GET'])
def get_products():
    products = Product.get_all_products()
    return jsonify(
        [{"product_id": product.product_id, "name": product.name, "price": product.price} for product in products])

@product_bp.route('/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = Product.get_product_by_id(product_id)
    if product:
        return jsonify({"product_id": product.product_id, "name": product.name, "price": product.price})
    return jsonify({"message": "Product not found"}), 404

@product_bp.route('/', methods=['POST'])
def create_product():
    data = request.get_json()
    product_id = len(Product.products_db) + 1
    name = data.get('name')
    price = data.get('price')
    if name and price:
        new_product = Product(product_id, name, price)
        return jsonify({"message": "Product created", "product_id": new_product.product_id}), 201
    return jsonify({"message": "Invalid data"}), 400

@product_bp.route('/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    if Product.delete_product(product_id):
        return jsonify({"message": "Product deleted"})
    return jsonify({"message": "Product not found"}), 404

@product_bp.route('/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()
    name = data.get('name')
    price = data.get('price')

    if Product.update_product(product_id, name, price):
        return jsonify({"message": "Product updated"})
    return jsonify({"message": "Product not found"}), 404