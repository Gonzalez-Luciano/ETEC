import pymysql
from DataBase import DataBase

class dbAlumnos(DataBase):
     def __init__(self,hostdb,userdb,db):
        super().__init__(hostdb,userdb,db)

     def crear_alumno(self,cuilAlumn,nombreAlumn,apellidoAlumn):
            sql="INSERT INTO alumnos (idAlumno, nombreAlumno, apellidoAlumno) VALUES ('{}', '{}', '{}')".format(cuilAlumn, nombreAlumn, apellidoAlumn)
                # ultimoId = len(self.__class__.lista)
                # self.__class__.lista.append( Alumno(str(ultimoId), alumnCompleto))
            try:
                self.cursor.execute(sql)
                self.connection.commit()
            except Exception as e:
                raise

database = dbAlumnos("localhost","root","test")