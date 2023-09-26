from ..models.usuario_model import Usuario

from flask import request

from decimal import Decimal

class UsuarioController:
    """usuario controller class"""

    @classmethod
    def get(cls, id_usuario):
        """Get a usuario by id"""
        usuario = Usuario(id_usuario=id_usuario)
        result = Usuario.get(usuario)
        if result is not None:
            return result.serialize(), 200
       
        
    @classmethod
    def get_all(cls):
        """Get all usaario"""
        usuario_objects = Usuario.get_all()
        usuario = []
        for usuario_object in usuario_objects:
            usuario.append(usuario_object.serialize())
            #usuario.append(usuario.serialize())
        return usuario, 200
    
    @classmethod
    def create(cls):
        """Create a new usuario"""
        data = request.json
        # TODO: Validate data
        if data.get('rental_rate') is not None:
            if isinstance(data.get('rental_rate'), int):
                data['rental_rate'] = Decimal(data.get('rental_rate'))/100
        
        if data.get('replacement_cost') is not None:
            if isinstance(data.get('replacement_cost'), int):
                data['replacement_cost'] = Decimal(data.get('replacement_cost'))/100

        usuario = Usuario(**data)
        Usuario.create(usuario)
        return {'message': 'usuario created successfully'}, 201

    @classmethod
    def update(cls, id_usuario):
        """Update a usuario"""
        data = request.json
        # TODO: Validate data
        if data.get('rental_rate') is not None:
            if isinstance(data.get('rental_rate'), int):
                data['rental_rate'] = Decimal(data.get('rental_rate'))/100
        
        if data.get('replacement_cost') is not None:
            if isinstance(data.get('replacement_cost'), int):
                data['replacement_cost'] = Decimal(data.get('replacement_cost'))/100
        
        data['id_usuario'] = id_usuario

        usuario = Usuario(**data)

        # TODO: Validate usuario exists
        Usuario.update(usuario)
        return {'message': 'Usuario updated successfully'}, 200
    
    @classmethod
    def delete(cls, id_usuario):
        """Delete a usuario"""
        usuario = Usuario(id_usuario=id_usuario)

        # TODO: Validate usuario exists
        Usuario.delete(usuario)
        return {'message': 'usuario deleted successfully'}, 204