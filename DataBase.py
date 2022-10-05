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
            db="test"
        )
        self.cursor = self.connection.cursor()
        
    # def crear_alumno(self,alumnoCuil,alumnoNombre,alumnoApellido):
    #     sql="INSERT INTO alumnos (idAlumno, nombreAlumno, apellidoAlumno) VALUES ('{}', '{}', '{}')".format(alumnoCuil, alumnoNombre, alumnoApellido)
    #         # ultimoId = len(self.__class__.lista)
    #         # self.__class__.lista.append( Alumno(str(ultimoId), alumnCompleto))
    #     try:
    #         self.cursor.execute(sql)
    #         self.connection.commit()
    #     except Exception as e:
    #         raise

    
database = DataBase()
