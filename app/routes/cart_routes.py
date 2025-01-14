from flask import Blueprint, request, jsonify
from app.models.cart import Cart

cart_bp = Blueprint('cart', __name__)
carts = {}

@cart_bp.route('/<int:user_id>', methods=['GET'])
def get_cart(user_id):
    cart = carts.get(user_id, Cart(user_id))
    return jsonify(cart.get_cart_details())

@cart_bp.route('/<int:user_id>/add', methods=['POST'])
def add_to_cart(user_id):
    product_id = request.json.get('product_id')
    quantity = request.json.get('quantity', 1)
    if not product_id:
        return jsonify({'error': 'Product ID is required'}), 400

    cart = carts.setdefault(user_id, Cart(user_id))
    cart.add_product(product_id, quantity)
    return jsonify({'message': 'Product added', 'cart': cart.get_cart_details()})

@cart_bp.route('/<int:user_id>/remove', methods=['POST'])
def remove_from_cart(user_id):
    product_id = request.json.get('product_id')
    if not product_id:
        return jsonify({'error': 'Product ID is required'}), 400

    cart = carts.setdefault(user_id, Cart(user_id))
    cart.remove_product(product_id)
    return jsonify({'message': 'Product removed', 'cart': cart.get_cart_details()})

@cart_bp.route('/<int:user_id>/clear', methods=['POST'])
def clear_cart(user_id):
    cart = carts.setdefault(user_id, Cart(user_id))
    cart.clear_cart()
    return jsonify({'message': 'Cart cleared', 'cart': cart.get_cart_details()})