from ..database import DatabaseConnection

class Servidor:
    """Servidor model class"""

    def __init__(self, id_servidor=None, nombre=None, descripcion=None, fecha_creacion=None):
        """Constructor method"""
        self.id_servidor = id_servidor
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_creacion = fecha_creacion

    def serialize(self):
        """Serialize object representation"""
        return {
            "id_servidor": self.id_servidor,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "fecha_creacion": self.fecha_creacion
        }

    @classmethod
    def get(cls, id_servidor):
        """Get a servidor by id"""
        query = "SELECT id_servidor, nombre, descripcion, fecha_creacion FROM servidores WHERE id_servidor = %s"
        params = (id_servidor,)
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return cls(*result)
        return None

    @classmethod
    def get_all(cls):
        """Get all servidores"""
        query = "SELECT id_servidor, nombre, descripcion, fecha_creacion FROM servidores"
        results = DatabaseConnection.fetch_all(query)

        servidores = []
        for result in results:
            servidores.append(cls(*result))
        return servidores

    @classmethod
    def create(cls, servidor):
        """Create a new servidor"""
        query = "INSERT INTO servidores (nombre, descripcion, fecha_creacion) VALUES (%s, %s, %s)"
        params = (servidor.nombre, servidor.descripcion, servidor.fecha_creacion)
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def update(cls, servidor):
        """Update a servidor"""
        query = "UPDATE servidores SET nombre = %s, descripcion = %s WHERE id_servidor = %s"
        params = (servidor.nombre, servidor.descripcion, servidor.id_servidor)
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def delete(cls, id_servidor):
        """Delete a servidor"""
        query = "DELETE FROM servidores WHERE id_servidor = %s"
        params = (id_servidor,)
        DatabaseConnection.execute_query(query, params=params)