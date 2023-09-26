from ..database import DatabaseConnection

class Usuario:
    """usuario model class"""

    def __init__(self, id_usuario=None, nombre=None, correo_electronico=None,
                 contrasenia=None, fecha_registro=None,  ultima_vez=None):
        
        """Constructor method"""
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.correo_electronico = correo_electronico
        self.contrasenia = contrasenia
        self.fecha_registro = fecha_registro
        self.ultima_vez = ultima_vez
        

    def serialize(self):
        """Serialize object representation
        Returns:
            dict: Object representation
        Note:
            - The last_update attribute is converted to string
            - The special_features attribute is converted to list if it is not
            null in the database. Otherwise, it is converted to None
            - The attributes rental_rate and replacement_cost are converted to
            int, because the Decimal type may lose precision if we convert
            it to float
        """
        if self.special_features is not None:
            special_features = list(self.special_features)
        else:
            special_features = None
        return {
            "id_usuario": self.id_usuario,
            "nombre": self.nombre,
            "correo_electronico": self.correo_electronico,
            "contrasenia": self.contrasenia,
            "fecha_registro": self.fecha_registro,
            "ultima_vez": self.ultima_vez,
            
        }

    @classmethod
    def get(cls, usuarios):
        """Get a usuario by id
        Args:
            - usuario (Usuario): Usuario object with the id attribute
        Returns:
            - Usuario: Usuario object
        """

        query = """SELECT id_usuario, nombre, correo_electronico, contrasenia,
        fecha_registro, original_language_id, rental_duration, rental_rate,
        length, ultima_vez, rating,  
        FROM talkhive.usuarios WHERE id_usuario = %s"""
        params = usuarios.id_usuario,
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return cls(*result)
        return None
       

        query = """SELECT id_usuario, nombre, correo_electronico, contrasenia,
        fecha_registro, ultima_vez,  
        FROM .talkhive.usuarios WHERE id_usuario = %s"""
        params = usuarios.id_usuario
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return cls(*result)
        return None

    @classmethod
    def get_all(cls):
        """Get all usuarios
        Returns:
            - list: List of Usiuario objects
        """
        query = """SELECT id_usuario, nombre, correo_electronico, contrasenia,
        fecha_registro, ultima_vez,  
        FROM .talkhive.usuarios"""
        results = DatabaseConnection.fetch_all(query)

        usuarios = []
        if results is not None:
            for result in results:
                usuarios.append(cls(*result))
        return usuarios

    @classmethod
    def create(cls, usuarios):
        """Create a new usuario
        Args:
            - usuario (Usuario): Usuario object
        """
        query = """INSERT INTO talkhive.usuarios (nombre, correo_electronico, contrasenia,
        fecha_registro, ultima_vez) 
        VALUES (%s, %s, %s, %s, %s)"""

        if usuarios.special_features is not None:
            special_features = ','.join(usuarios.special_features)
        else:
            special_features = None
        params = usuarios.nombre, usuarios.correo_electronico, usuarios.contrasenia, \
                 usuarios.fecha_registro, usuarios.ultima_vez,special_features
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def update(cls, usuarios):
        """Update a usuarios
        Args:
            - usuarios (usuarios): Usuarios object
        """
        query = """UPDATE talkhive.usuarios SET nombre = %s, correo_electronico = %s,
        contrasenia = %s, fecha_registro = %s, ultima_vez = %s,
        WHERE id_usuario = %s"""
        if usuarios.special_features is not None:
            special_features = ','.join(usuarios.special_features)
        else:
            special_features = None
        params = usuarios.nombre, usuarios.correo_electronico, usuarios.contrasenia, \
                 usuarios.fecha_registro, usuarios.ultima_vez, usuarios.id_usuario,special_features
        DatabaseConnection.execute_query(query, params=params): usuarios.object
        """
        allowed_columns = {'nombre', 'correo_electronico', 'contrasenia',
                           'fecha_registro', 'ultima_vez',
                           'special_features'}
        query_parts = []
        params = []
        for key, value in film.__dict__.items():
            if key in allowed_columns and value is not None:
                if key == 'special_features':
                    if len(value) == 0:
                        value = None
                    else:
                        value = ','.join(value)
                query_parts.append(f"{key} = %s")
                params



from ..database import DatabaseConnection"""


    #@classmethod
    #def update(cls, film):
        """Update a film
        Args:
            - film (Film): Film object
        """
        """allowed_columns = {'title', 'description', 'release_year',
                           'language_id', 'original_language_id',
                           'rental_duration', 'rental_rate', 'length',
                           'replacement_cost', 'rating', 'special_features'}
        query_parts = []
        params = []
        for key, value in film.__dict__.items():
            if key in allowed_columns and value is not None:
                if key == 'special_features':
                    if len(value) == 0:
                        value = None
                    else:
                        value = ','.join(value)
                query_parts.append(f"{key} = %s")
                params.append(value)
        params.append(film.film_id)

        query = "UPDATE sakila.film SET " + ", ".join(query_parts) + " WHERE film_id = %s"
        DatabaseConnection.execute_query(query, params=params)"""
    
    #@classmethod
    #def delete(cls, film):
        """Delete a film
        Args:
            - film (Film): Film object with the id attribute
        """
        """ query = "DELETE FROM sakila.film WHERE film_id = %s"
        params = film.film_id,
        DatabaseConnection.execute_query(query, params=params)"""