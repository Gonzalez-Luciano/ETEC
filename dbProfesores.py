import pymysql
from DataBase import DataBase

class dbPrfesores(DataBase):
     def __init__(self,hostdb,userdb,db):
        super().__init__(hostdb,userdb,db)

     def crear_profesor(self,cuilProfesor,nombreProfesor,apellidoProfesor,correoProfesor):
            sql="INSERT INTO profesores (idProfesor, nombreProfesor, apellidoProfesor, correoProfesor) VALUES ('{}', '{}', '{}','{}')".format(cuilProfesor, nombreProfesor, apellidoProfesor,correoProfesor)
                # ultimoId = len(self.__class__.lista)
                # self.__class__.lista.append( Alumno(str(ultimoId), alumnCompleto))
            try:
                self.cursor.execute(sql)
                self.connection.commit()
            except Exception as e:
                raise

database=dbPrfesores("localhost","root","test")