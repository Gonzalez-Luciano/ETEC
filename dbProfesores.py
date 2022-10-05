import pymysql
import DataBase

class dbPrfesores():
     def __init__(self):
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            db="test",
        )
        self.cursor = self.connection.cursor()

     def crear_profesor(self,cuilProfesor,nombreProfesor,apellidoProfesor,correoProfesor):
            sql="INSERT INTO profesores (idProfesor, nombreProfesor, apellidoProfesor, correoProfesor) VALUES ('{}', '{}', '{}','{}')".format(cuilProfesor, nombreProfesor, apellidoProfesor,correoProfesor)
                # ultimoId = len(self.__class__.lista)
                # self.__class__.lista.append( Alumno(str(ultimoId), alumnCompleto))
            try:
                self.cursor.execute(sql)
                self.connection.commit()
            except Exception as e:
                raise