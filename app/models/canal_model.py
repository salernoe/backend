from ..database import DatabaseConnection

class Canal:
    """Canal model class"""

    def __init__(self, id_canal=None, nombre=None, tipo=None, id_servidor=None, fecha_creacion=None):
        """Constructor method"""
        self.id_canal = id_canal
        self.nombre = nombre
        self.tipo = tipo
        self.id_servidor = id_servidor
        self.fecha_creacion = fecha_creacion

    def serialize(self):
        """Serialize object representation"""
        return {
            "id_canal": self.id_canal,
            "nombre": self.nombre,
            "tipo": self.tipo,
            "id_servidor": self.id_servidor,
            "fecha_creacion": self.fecha_creacion
        }

    @classmethod
    def get(cls, id_canal):
        """Get a canal by id"""
        query = "SELECT id_canal, nombre, tipo, id_servidor, fecha_creacion FROM canales WHERE id_canal = %s"
        params = (id_canal,)
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return cls(*result)
        return None

    @classmethod
    def get_all(cls):
        """Get all canales"""
        query = "SELECT id_canal, nombre, tipo, id_servidor, fecha_creacion FROM canales"
        results = DatabaseConnection.fetch_all(query)

        canales = []
        for result in results:
            canales.append(cls(*result))
        return canales

    @classmethod
    def create(cls, canal):
        """Create a new canal"""
        query = "INSERT INTO canales (nombre, tipo, id_servidor, fecha_creacion) VALUES (%s, %s, %s, %s)"
        params = (canal.nombre, canal.tipo, canal.id_servidor, canal.fecha_creacion)
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def update(cls, canal):
        """Update a canal"""
        query = "UPDATE canales SET nombre = %s, tipo = %s WHERE id_canal = %s"
        params = (canal.nombre, canal.tipo, canal.id_canal)
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def delete(cls, id_canal):
        """Delete a canal"""
        query = "DELETE FROM canales WHERE id_canal = %s"
        params = (id_canal,)
        DatabaseConnection.execute_query(query, params=params)