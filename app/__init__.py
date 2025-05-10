# C:\Users\ianes\Desktop\AS Cloud\app\__init__.py

from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()

# Configuração do Login
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message = 'Por favor, faça login para acessar esta página.'
login_manager.login_message_category = 'info'

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)  # inicializa aqui

    # registra blueprints
    from .auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')
    from .cars import cars_bp
    app.register_blueprint(cars_bp, url_prefix='/cars')

    @app.route('/')
    def index():
        return redirect(url_for('cars.list_cars'))

    # cria tablas no startup
    with app.app_context():
        db.create_all()

    return app

# loader de usuario fica no modulo raiz
from app.models import User
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
