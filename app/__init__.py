from flask import Flask
from flask_cors import CORS
from config import Config
from .routes.error_handlers import errors
from .models.exeptions import UsuarioNotFound
from .routes.usuario_bp import login_bp


from .database import DatabaseConnection

def init_app():
    """Crea y configura la aplicación Flask"""
    
    app = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)
    
    CORS(app, supports_credentials=True)

    app.config.from_object(
        Config
    )
    
    app.register_blueprint(errors)
    
    DatabaseConnection.set_config(app.config)

    app.register_blueprint(login_bp, url_prefix = '/login')
    
       
    
    return app



"""from flask import Flask, jsonify, request
from flask_cors import CORS
from config import Config
from .database import DatabaseConnection
import mysql.connector
from .models.exeptions import UsuarioNotFound


def init_app():
    #Crea y configura la aplicación Flask
    
    app = Flask(__name__, static_folder=Config.STATIC_FOLDER, template_folder=Config.TEMPLATE_FOLDER)
    
    CORS(app, supports_credentials=True)

    app.config.from_object(Config)

    DatabaseConnection.set_config(app.config)
    
      
    
   # Un endpoint que dice 'Hola Mundo!'
    @app.route('/')
    def hello_world():
     return 'Hola Mundo!'
 
    @app.route('/usuarios/<int:id_usuario>', methods=['GET'])
        
    def usuario_exists(id_usuario): 
            cursor = DatabaseConnection.cursor()
            query = "SELECT COUNT(*) FROM films WHERE id = %s"
            cursor.execute(query, (id_usuario,))
            count = cursor.fetchone()[0]
            cursor.close()
            return count > 0

 
    def get_usuarios_by_id(id_usuario):
        
        if not UsuarioNotFound(id_usuario):
            raise id_usuario(id_usuario)

        # Si la película existe, devuelve los detalles de la película en la respuesta
        return jsonify({
            "id_usuario": id_usuario,
            
        })
 
    return app
 
 
 
 
 
 
 """