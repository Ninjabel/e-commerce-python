from flask import Flask
from app.routes.main_routes import main_bp
from app.routes.user_routes import user_bp
from app.routes.product_routes import product_bp
from app.routes.order_routes import order_bp
from app.routes.cart_routes import cart_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main_bp)
    app.register_blueprint(user_bp, url_prefix='/users')
    app.register_blueprint(product_bp, url_prefix='/products')
    app.register_blueprint(order_bp, url_prefix='/orders')
    app.register_blueprint(cart_bp, url_prefix='/cart')
    return app