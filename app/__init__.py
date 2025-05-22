from flask import Flask
from app.models import init_db

def create_app():
    app = Flask(__name__)
    app.config['DATABASE'] = 'database/dts.db'
    with app.app_context():
        init_db()
    from app.routes import bp
    app.register_blueprint(bp)
    return app
