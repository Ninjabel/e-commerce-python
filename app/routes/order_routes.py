from flask import Blueprint, jsonify, request
from app.models.order import Order

order_bp = Blueprint('order', __name__)


@order_bp.route('/', methods=['GET'])
def get_orders():
    orders = Order.get_all_orders()
    return jsonify([{
        "order_id": order.order_id,
        "user_id": order.user_id,
        "products": order.products
    } for order in orders])


@order_bp.route('/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = Order.get_order_by_id(order_id)
    if order:
        return jsonify({
            "order_id": order.order_id,
            "user_id": order.user_id,
            "products": order.products
        })
    return jsonify({"message": "Order not found"}), 404


@order_bp.route('/', methods=['POST'])
def create_order():
    data = request.get_json()
    order_id = len(Order.orders_db) + 1
    user_id = data.get('user_id')
    products = data.get('products')
    if user_id and products:
        new_order = Order(order_id, user_id, products)
        return jsonify({"message": "Order created", "order_id": new_order.order_id}), 201
    return jsonify({"message": "Invalid data"}), 400


@order_bp.route('/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    if Order.delete_order(order_id):
        return jsonify({"message": "Order deleted"})
    return jsonify({"message": "Order not found"}), 404


@order_bp.route('/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    data = request.get_json()
    user_id = data.get('user_id')
    products = data.get('products')

    if Order.update_order(order_id, user_id, products):
        return jsonify({"message": "Order updated"})
    return jsonify({"message": "Order not found"}), 404