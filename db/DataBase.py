import pymysql
import cryptography
from cryptography.exceptions import InternalError

class DataBase:
    def __init__(self, hostdb, userdb, db, password):
        self.hostdb = hostdb
        self.userdb = userdb
        self.db = db
        self.password = password
        try:
            self.connection = pymysql.connect(
                host=hostdb,
                user=userdb,
                password=password,
                database=db
            )
            self.cursor = self.connection.cursor()
            print("Conexión establecida.")
        except (pymysql.err.OperationalError, InternalError) as e:
            print(f"Error de conexión: {e}")
            self.create_database_and_tables()

    def create_database_and_tables(self):
        try:
            connection_root = pymysql.connect(
                host=self.hostdb,
                user='root',
                password=self.password
            )
            cursor_root = connection_root.cursor()

            # Crear la base de datos si no existe
            cursor_root.execute(f"CREATE DATABASE IF NOT EXISTS {self.db}")

            # Crear el usuario EtecUser si no existe y otorgar los permisos necesarios
            cursor_root.execute(f"CREATE USER IF NOT EXISTS 'EtecUser'@'localhost' IDENTIFIED BY '1234'")
            cursor_root.execute(f"GRANT ALL PRIVILEGES ON {self.db}.* TO 'EtecUser'@'localhost'")
            cursor_root.execute("FLUSH PRIVILEGES")

            # Aplicar los cambios
            connection_root.commit()
            connection_root.close()

            # Conectar a la base de datos recién creada
            self.connection = pymysql.connect(
                host=self.hostdb,
                user=self.userdb,
                password=self.password,
                database=self.db
            )
            self.cursor = self.connection.cursor()

            # Crear las tablas si no existen
            self.create_tables()

            print("Base de datos, usuario y tablas creados exitosamente.")

        except (pymysql.err.OperationalError, InternalError) as e:
            print(f"Error al crear la base de datos, usuario y/o tablas: {e}")
            raise ConnectionError("No se pudo establecer la conexión con la base de datos. Por favor, asegúrate de tener XAMPP o Workbench abierto para establecer la conexión.")

    def create_tables(self):
        try:
            sql_queries = [
                    """
                    CREATE TABLE IF NOT EXISTS alumnos (
                    idAlumno int(11) NOT NULL AUTO_INCREMENT,
                    cuilAlumno varchar(50) NOT NULL,
                    nombreAlumno varchar(50) NOT NULL,
                    apellidoAlumno varchar(50) NOT NULL,
                    active tinyint(1) NOT NULL,
                    PRIMARY KEY (idAlumno)
                    )
                    """,
                    """
                    CREATE TABLE IF NOT EXISTS alumnos_materias (
                    idAlumnos_materias int(11) NOT NULL AUTO_INCREMENT,
                    idAlumno int(11) NOT NULL,
                    idMateria int(11) NOT NULL,
                    active tinyint(1) NOT NULL,
                    PRIMARY KEY (idAlumnos_materias)
                    )
                    """,
                    """
                    CREATE TABLE IF NOT EXISTS materias (
                    idMateria int(11) NOT NULL AUTO_INCREMENT,
                    nombreMateria varchar(50) NOT NULL,
                    descripcionMateria text NOT NULL,
                    active tinyint(1) NOT NULL,
                    PRIMARY KEY (idMateria)
                    )
                    """,
                    """
                    CREATE TABLE IF NOT EXISTS profesores (
                    idProfesor int(11) NOT NULL AUTO_INCREMENT,
                    cuilProfesor varchar(50) NOT NULL,
                    nombreProfesor varchar(50) NOT NULL,
                    apellidoProfesor varchar(50) NOT NULL,
                    correoProfesor varchar(50) NOT NULL,
                    active tinyint(1) NOT NULL,
                    PRIMARY KEY (idProfesor)
                    )
                    """,
                    """
                    CREATE TABLE IF NOT EXISTS profesores_materias (
                    idProfesores_materias int(11) NOT NULL AUTO_INCREMENT,
                    idProfesor int(11) NOT NULL,
                    idMateria int(11) NOT NULL,
                    active tinyint(1) NOT NULL,
                    PRIMARY KEY (idProfesores_materias)
                    )
                    """
                ]

            for query in sql_queries:
                self.cursor.execute(query)
            self.connection.commit()
        except pymysql.err.OperationalError as e:
            # Si hay un error, deshacer cualquier cambio
            self.connection.rollback()
            print(f"Error al crear las tablas: {e}")

        


    

