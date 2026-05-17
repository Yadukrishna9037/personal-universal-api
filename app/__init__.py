from flask import Flask

def create_app():
    app = Flask(__name__)

    # Import and register the routes
    from app.routes import api_bp
    app.register_blueprint(api_bp)

    return app