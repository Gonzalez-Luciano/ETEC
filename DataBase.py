import pymysql
"""Tabla:Alumno(
    id primary key: CUIL
    nombre: VarChar:50
    materia: id de tabla Materia
    turno: Mañana o tarde(Int)
    Año:Varchar)"""
    
"""Tabla:Profesor(
id primary key: CUIL
nombre: VarChar:50
materia: id de tabla Materia
turno: Mañana o tarde(Int)
Año:Varchar)"""

"""Tabla:Materia(
id primary key: por cada materia
nombre: VarChar:50
Año:Varchar)"""

class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            password="admin",
            db="prueba"
        )
        self.cursor = self.connection.cursor()


database = DataBase()