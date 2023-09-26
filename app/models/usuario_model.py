from ..database import DatabaseConnection

class Usuario:
    """Usuario model class"""

    def __init__(self, id_usuario=None, nombre=None, correo_electronico=None,
                 cantrasenia=None, fecha_registro=None, ultima_vez=None):
        """Constructor method"""
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.correo_electronico = correo_electronico
        self.cantrasenia = cantrasenia
        self.fecha_registro = fecha_registro
        self.ultima_vez = ultima_vez

    def serialize(self):
        """Serialize object representation"""
        return {
            "id_usuario": self.id_usuario,
            "nombre": self.nombre,
            "correo_electronico": self.correo_electronico,
            "cantrasenia": self.cantrasenia,
            "fecha_registro": self.fecha_registro,
            "ultima_vez": self.ultima_vez
        }

    @classmethod
    def get(cls, usuarios):
        """Get a usuario by id"""
        query = """SELECT id_usuario, nombre, correo_electronico, cantrasenia,
        fecha_registro, ultima_vez
        FROM talkhive.usuarios WHERE id_usuario = %s"""
        params = (usuarios.id_usuario,)
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return cls(*result)
        return None

    @classmethod
    def get_all(cls):
        """Get all usuarios"""
        query = """SELECT id_usuario, nombre, correo_electronico, cantrasenia,
        fecha_registro, ultima_vez
        FROM talkhive.usuarios"""
        results = DatabaseConnection.fetch_all(query)

        usuarios = []
        for result in results:
            usuarios.append(cls(*result))
        return usuarios

    @classmethod
    def create(cls, usuarios):
        """Create a new usuario"""
        query = """INSERT INTO talkhive.usuarios (nombre, correo_electronico, cantrasenia,
        fecha_registro, ultima_vez) 
        VALUES (%s, %s, %s, %s, %s)"""
        params = (
            usuarios.nombre, usuarios.correo_electronico,
            usuarios.cantrasenia, usuarios.fecha_registro, usuarios.ultima_vez
        )
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def update(cls, usuarios):
        """Update a usuario"""
        query = """UPDATE talkhive.usuarios SET nombre = %s, correo_electronico = %s,
        cantrasenia = %s, fecha_registro = %s, ultima_vez = %s
        WHERE id_usuario = %s"""
        params = (
            usuarios.nombre, usuarios.correo_electronico,
            usuarios.cantrasenia, usuarios.fecha_registro,
            usuarios.ultima_vez, usuarios.id_usuario
        )
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def delete(cls, usuarios):
        """Delete a usuario"""
        query = "DELETE FROM talkhive.usuarios WHERE id_usuario = %s"
        params = (usuarios.id_usuario,)
        DatabaseConnection.execute_query(query, params=params)