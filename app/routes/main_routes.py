from flask import Blueprint, Response
import json

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    message = {
        "message": "Welcome to the e-commerce API! Use the endpoints /users/, /products/, /cart/, /orders/."
    }
    return Response(json.dumps(message, ensure_ascii=False), mimetype='application/json')