from ..models.usuario_model import Usuario
from flask import request
from decimal import Decimal

class UsuarioController:
    """Usuario controller class"""

    @classmethod
    def get(cls, id_usuario):
        """Get a usuario by id"""
        try:
            usuario = Usuario(id_usuario=id_usuario)
            result = Usuario.get(usuario)
            if result is not None:
                return result.serialize(), 200
            else:
                return {'message': 'Usuario not found'}, 404
        except Exception as e:
            return {'error': str(e)}, 500

    @classmethod
    def get_all(cls):
        """Get all usuarios"""
        try:
            usuario_objects = Usuario.get_all()
            usuarios = [usuario.serialize() for usuario in usuario_objects]
            return usuarios, 200
        except Exception as e:
            return {'error': str(e)}, 500

    @classmethod
    def create(cls):
        """Create a new usuario"""
        try:
            data = request.json
            # TODO: Validate data

            # Convert rental_rate and replacement_cost to Decimal
            for field in ['rental_rate', 'replacement_cost']:
                if data.get(field) is not None and isinstance(data.get(field), int):
                    data[field] = Decimal(data[field]) / 100

            usuario = Usuario(**data)
            Usuario.create(usuario)
            return {'message': 'Usuario created successfully'}, 201
        except Exception as e:
            return {'error': str(e)}, 500

    @classmethod
    def update(cls, id_usuario):
        """Update a usuario"""
        try:
            data = request.json
            # TODO: Validate data

            # Convert rental_rate and replacement_cost to Decimal
            for field in ['rental_rate', 'replacement_cost']:
                if data.get(field) is not None and isinstance(data.get(field), int):
                    data[field] = Decimal(data[field]) / 100

            data['id_usuario'] = id_usuario
            usuario = Usuario(**data)

            # TODO: Validate usuario exists
            Usuario.update(usuario)
            return {'message': 'Usuario updated successfully'}, 200
        except Exception as e:
            return {'error': str(e)}, 500

    @classmethod
    def delete(cls, id_usuario):
        """Delete a usuario"""
        try:
            usuario = Usuario(id_usuario=id_usuario)

            # TODO: Validate usuario exists
            Usuario.delete(usuario)
            return {'message': 'Usuario deleted successfully'}, 204
        except Exception as e:
            return {'error': str(e)}, 500