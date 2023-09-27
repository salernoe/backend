from flask import Blueprint, request, jsonify
from ..models.exeptions import UsuarioNotFound 
from ..database import DatabaseConnection

import bcrypt  

login_bp = Blueprint('login_bp', __name__)

@login_bp.route('/login', methods=['POST'])  # Cambia la URL a /login
def login():
    try:
        # Obtén los datos del formulario de inicio de sesión
        data = request.get_json()
        nombre = data.get('nombre')
        cantrasenia = data.get('cantrasenia')

        # Consulta la base de datos para obtener la contraseña almacenada
        query = "SELECT cantrasenia FROM talkhive.usuarios WHERE nombre = %s"
        params = (nombre,)
        result = DatabaseConnection.fetch_one(query, params)

        if result:
            cantrasenia_hash = result[0]

            # Compara la contraseña ingresada con el hash almacenado
            if bcrypt.checkpw(cantrasenia.encode('utf-8'), cantrasenia_hash.encode('utf-8')):
                return jsonify({'message': f'Inicio de sesión exitoso para {nombre}'}), 200
            else:
                raise UsuarioNotFound  # Las contraseñas no coinciden
        else:
            raise UsuarioNotFound  # El usuario no se encuentra

    except UsuarioNotFound:
        # Maneja la excepción si las credenciales son incorrectas o el usuario no se encuentra
        return jsonify({'error': 'Usuario no encontrado o credenciales incorrectas'}), 401
    except Exception as e:
        # Maneja otras excepciones
        return jsonify({'error': 'Error interno'}), 500