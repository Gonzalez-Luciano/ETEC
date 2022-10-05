import pymysql
import DataBase

class dbAlumnos():
     def __init__(self):
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            db="test",
        )
        self.cursor = self.connection.cursor()

     def crear_alumno(self,cuilAlumn,nombreAlumn,apellidoAlumn):
            sql="INSERT INTO alumnos (idAlumno, nombreAlumno, apellidoAlumno) VALUES ('{}', '{}', '{}')".format(cuilAlumn, nombreAlumn, apellidoAlumn)
                # ultimoId = len(self.__class__.lista)
                # self.__class__.lista.append( Alumno(str(ultimoId), alumnCompleto))
            try:
                self.cursor.execute(sql)
                self.connection.commit()
            except Exception as e:
                raise