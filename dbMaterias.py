import pymysql
from DataBase import DataBase

class dbMaterias(DataBase):
     def __init__(self,hostdb,userdb,db):
        super().__init__(hostdb,userdb,db)

     def crear_materia(self,nombreMateria,descripMateria):
            sql="INSERT INTO materias (idMateria, nombreMateria, descripciónMateria) VALUES (NULL, '{}', '{}')".format(nombreMateria, descripMateria)
                # ultimoId = len(self.__class__.lista)
                # self.__class__.lista.append( Alumno(str(ultimoId), alumnCompleto))
            try:
                self.cursor.execute(sql)
                self.connection.commit()
            except Exception as e:
                raise

database = dbMaterias("localhost","root","test")