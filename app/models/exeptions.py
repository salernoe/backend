from flask import jsonify
from ..database import DatabaseConnection

class CustomException(Exception):
    def __init__(self, status_code, name = "Custom Error", description 
    = 'Error'): 
        super().__init__()
        self.description = description
        self.name = name
        self.status_code = status_code
    def get_response(self):
        response = jsonify({
        'error': {
        'code': self.status_code,
        'name': self.name,
        'description': self.description,
        }
        })
        response.status_code = self.status_code
        return response


class UsuarioNotFound(CustomException):
    def __init__(self, id_usuario):
        super().__init__(f" User with ID {id_usuario} not found")
        self.id_usuario = id_usuario.mNotFound(CustomException);
    
    
    """def __init__(self, id_usuario):
        super().__init__(f" Film with ID {id_usuario} not found")
        self.id_usuario = id_usuario"""
    