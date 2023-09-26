from flask import Blueprint, request, jsonify
from ..models.exeptions import UsuarioNotFound 
from ..database import DatabaseConnection

login_bp = Blueprint('login_bp', __name__)

@login_bp.route('/login/<usuario>', methods=['POST'])
def login():
    try:
        # Obtén los datos del formulario de inicio de sesión
        data = request.get_json()
        usuario = data.get('usuario')
        contrasenia = data.get('contrasenia')

        # Consulta la base de datos para verificar las credenciales
        query = "SELECT nombre FROM usuarios WHERE usuario = %s AND contrasenia = %s"
        params = (usuario, contrasenia)
        result = DatabaseConnection.fetch_one(query, params)

        if result:
            nombre_usuario = result[0]
            return jsonify({'message': f'Inicio de sesión exitoso para {nombre_usuario}'}), 200
        else:
            raise UsuarioNotFound

    except UsuarioNotFound:
        # Maneja la excepción si las credenciales son incorrectas o el usuario no se encuentra
        return jsonify({'error': 'Usuario no encontrado o credenciales incorrectas'}), 401
    except Exception as e:
        # Maneja otras excepciones
        return jsonify({'error': 'Error interno'}), 500