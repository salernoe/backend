from flask import Flask
from flask_cors import CORS
from config import Config
from .routes.error_handlers import errors
from .models.exeptions import UsuarioNotFound
from .routes.usuario_bp import usuario_bp
from .routes.login_bp import login_bp
from .routes.servidor_bp import servidor_bp
from .routes.chats_bp import chat_bp
from .routes.canales_bp import canal_bp
from .database import DatabaseConnection

def init_app():
    """Crea y configura la aplicación Flask"""

    app = Flask(__name__, static_folder=Config.STATIC_FOLDER, template_folder=Config.TEMPLATE_FOLDER)

    CORS(app, supports_credentials=True)

    app.config.from_object(Config)

    app.register_blueprint(errors)

    DatabaseConnection.set_config(app.config)

    app.register_blueprint(usuario_bp, url_prefix='/usuario')
    app.register_blueprint(login_bp, url_prefix='/login')
    app.register_blueprint(servidor_bp, url_prefix='/servidor')
    app.register_blueprint(chat_bp, url_prefix='/chats')
    app.register_blueprint(canal_bp, url_prefix='/canales')
    
    
    
    return app


