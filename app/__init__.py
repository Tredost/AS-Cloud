from flask import Flask, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_restx import Api as RestXApi
from config import Config

# Instâncias das extensões
db = SQLAlchemy()
login_manager = LoginManager()

# Configuração do Flask-Login
login_manager.login_view = 'auth.login'
login_manager.login_message = 'Por favor, faça login para acessar esta página.'
login_manager.login_message_category = 'info'

# Instância do Flask-RESTX para Swagger UI
rest_api = RestXApi(
    title='Galeria de Fotos API',
    version='1.0',
    description='CRUD de artistas, obras e exposições com Swagger UI',
    doc='/api/docs/'
)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializa extensões
    db.init_app(app)
    login_manager.init_app(app)
    rest_api.init_app(app)

    # Registra namespaces da API
    from app.api.auth        import auth_ns
    from app.api.artists     import artists_ns
    from app.api.artworks    import artworks_ns
    from app.api.exhibitions import exhibitions_ns

    rest_api.add_namespace(auth_ns,        path='/api/auth')
    rest_api.add_namespace(artists_ns,     path='/api/artists')
    rest_api.add_namespace(artworks_ns,    path='/api/artworks')
    rest_api.add_namespace(exhibitions_ns, path='/api/exhibitions')

    # Rota raiz redireciona para a documentação Swagger
    @app.route('/')
    def index():
        return redirect('/api/docs')

    # Cria tabelas se não existirem
    with app.app_context():
        db.create_all()

    return app

# Loader de usuário para Flask-Login
from app.models import User
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
