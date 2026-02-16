from flask import Flask


def create_app():
    app = Flask(__name__)

    from app.routes import math_bp

    app.register_blueprint(math_bp)

    return app
