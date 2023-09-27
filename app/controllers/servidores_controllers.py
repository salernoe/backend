from ..models.servidor_model import Servidor  
from flask import request
from decimal import Decimal

class ServidorController:
    """Servidor controller class"""

    @classmethod
    def get(cls, id_servidor):
        """Get a servidor by id"""
        try:
            servidor = Servidor(id_servidor=id_servidor)
            result = Servidor.get(servidor)
            if result is not None:
                return result.serialize(), 200
            else:
                return {'message': 'Servidor not found'}, 404
        except Exception as e:
            return {'error': str(e)}, 500

    @classmethod
    def get_all(cls):
        """Get all servidores"""
        try:
            servidor_objects = Servidor.get_all()
            servidores = [servidor.serialize() for servidor in servidor_objects]
            return servidores, 200
        except Exception as e:
            return {'error': str(e)}, 500

    @classmethod
    def create(cls):
        """Create a new servidor"""
        try:
            data = request.json
            # TODO: Validate data

            servidor = Servidor(**data)
            Servidor.create(servidor)
            return {'message': 'Servidor created successfully'}, 201
        except Exception as e:
            return {'error': str(e)}, 500

    @classmethod
    def update(cls, id_servidor):
        """Update a servidor"""
        try:
            data = request.json
            # TODO: Validate data

            data['id_servidor'] = id_servidor
            servidor = Servidor(**data)

            # TODO: Validate servidor exists
            Servidor.update(servidor)
            return {'message': 'Servidor updated successfully'}, 200
        except Exception as e:
            return {'error': str(e)}, 500

    @classmethod
    def delete(cls, id_servidor):
        """Delete a servidor"""
        try:
            servidor = Servidor(id_servidor=id_servidor)

            # TODO: Validate servidor exists
            Servidor.delete(servidor)
            return {'message': 'Servidor deleted successfully'}, 204
        except Exception as e:
            return {'error': str(e)}, 500