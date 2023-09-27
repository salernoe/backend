from flask import request, jsonify
from ..models.canal_model import Canal  # Asegúrate de importar la clase correcta

class CanalController:
    """Canal controller class"""

    @classmethod
    def get(cls, id_canal):
        """Get a canal by id"""
        try:
            canal = Canal(id_canal=id_canal)
            result = Canal.get(canal)
            if result is not None:
                return result.serialize(), 200
            else:
                return {'message': 'Canal not found'}, 404
        except Exception as e:
            return {'error': str(e)}, 500

    @classmethod
    def get_all(cls):
        """Get all canales"""
        try:
            canal_objects = Canal.get_all()
            canales = [canal.serialize() for canal in canal_objects]
            return canales, 200
        except Exception as e:
            return {'error': str(e)}, 500

    @classmethod
    def create(cls):
        """Create a new canal"""
        try:
            data = request.json
            # TODO: Validate data

            canal = Canal(**data)
            Canal.create(canal)
            return {'message': 'Canal created successfully'}, 201
        except Exception as e:
            return {'error': str(e)}, 500

    @classmethod
    def update(cls, id_canal):
        """Update a canal"""
        try:
            data = request.json
            # TODO: Validate data

            data['id_canal'] = id_canal
            canal = Canal(**data)

            # TODO: Validate canal exists
            Canal.update(canal)
            return {'message': 'Canal updated successfully'}, 200
        except Exception as e:
            return {'error': str(e)}, 500

    @classmethod
    def delete(cls, id_canal):
        """Delete a canal"""
        try:
            canal = Canal(id_canal=id_canal)

            # TODO: Validate canal exists
            Canal.delete(canal)
            return {'message': 'Canal deleted successfully'}, 204
        except Exception as e:
            return {'error': str(e)}, 500