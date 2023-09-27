from ..database import DatabaseConnection

class Chat:
    """Chat model class"""

    def __init__(self, id_mensaje=None, contenido=None, fecha_hora=None, id_usuario_envia=None, id_canal_enviado=None):
        """Constructor method"""
        self.id_mensaje = id_mensaje
        self.contenido = contenido
        self.fecha_hora = fecha_hora
        self.id_usuario_envia = id_usuario_envia
        self.id_canal_enviado = id_canal_enviado

    def serialize(self):
        """Serialize object representation"""
        return {
            "id_mensaje": self.id_mensaje,
            "contenido": self.contenido,
            "fecha_hora": self.fecha_hora,
            "id_usuario_envia": self.id_usuario_envia,
            "id_canal_enviado": self.id_canal_enviado
        }

    @classmethod
    def get(cls, id_mensaje):
        """Get a chat message by id"""
        query = "SELECT id_mensaje, contenido, fecha_hora, id_usuario_envia, id_canal_enviado FROM chats WHERE id_mensaje = %s"
        params = (id_mensaje,)
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return cls(*result)
        return None

    @classmethod
    def get_all(cls):
        """Get all chat messages"""
        query = "SELECT id_mensaje, contenido, fecha_hora, id_usuario_envia, id_canal_enviado FROM chats"
        results = DatabaseConnection.fetch_all(query)

        chat_messages = []
        for result in results:
            chat_messages.append(cls(*result))
        return chat_messages

    @classmethod
    def create(cls, chat_message):
        """Create a new chat message"""
        query = "INSERT INTO chats (contenido, fecha_hora, id_usuario_envia, id_canal_enviado) VALUES (%s, %s, %s, %s)"
        params = (chat_message.contenido, chat_message.fecha_hora, chat_message.id_usuario_envia, chat_message.id_canal_enviado)
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def update(cls, chat_message):
        """Update a chat message"""
        query = "UPDATE chats SET contenido = %s, fecha_hora = %s WHERE id_mensaje = %s"
        params = (chat_message.contenido, chat_message.fecha_hora, chat_message.id_mensaje)
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def delete(cls, id_mensaje):
        """Delete a chat message"""
        query = "DELETE FROM chats WHERE id_mensaje = %s"
        params = (id_mensaje,)
        DatabaseConnection.execute_query(query, params=params)