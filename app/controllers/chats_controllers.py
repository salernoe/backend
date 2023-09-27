from ..models.chat_model import Chat  # Asegúrate de importar la clase correcta
from flask import request

class ChatController:
    """Chat controller class"""

    @classmethod
    def get(cls, id_chat):
        """Get a chat by id"""
        try:
            chat = Chat(id_chat=id_chat)
            result = Chat.get(chat)
            if result is not None:
                return result.serialize(), 200
            else:
                return {'message': 'Chat not found'}, 404
        except Exception as e:
            return {'error': str(e)}, 500

    @classmethod
    def get_all(cls):
        """Get all chats"""
        try:
            chat_objects = Chat.get_all()
            chats = [chat.serialize() for chat in chat_objects]
            return chats, 200
        except Exception as e:
            return {'error': str(e)}, 500

    @classmethod
    def create(cls):
        """Create a new chat"""
        try:
            data = request.json
            # TODO: Validate data

            chat = Chat(**data)
            Chat.create(chat)
            return {'message': 'Chat created successfully'}, 201
        except Exception as e:
            return {'error': str(e)}, 500

    @classmethod
    def update(cls, id_chat):
        """Update a chat"""
        try:
            data = request.json
            # TODO: Validate data

            data['id_chat'] = id_chat
            chat = Chat(**data)

            # TODO: Validate chat exists
            Chat.update(chat)
            return {'message': 'Chat updated successfully'}, 200
        except Exception as e:
            return {'error': str(e)}, 500

    @classmethod
    def delete(cls, id_chat):
        """Delete a chat"""
        try:
            chat = Chat(id_chat=id_chat)

            # TODO: Validate chat exists
            Chat.delete(chat)
            return {'message': 'Chat deleted successfully'}, 204
        except Exception as e:
            return {'error': str(e)}, 500