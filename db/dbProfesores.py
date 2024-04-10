import pymysql
from db.DataBase import DataBase
import cryptography

class dbProfesores(DataBase):
    def __init__(self,hostdb,userdb,db,password):
        super().__init__(hostdb,userdb,db,password)

    def crear_profesor(self,cuilProfesor,nombreProfesor,apellidoProfesor,correoProfesor):
        sql="INSERT INTO profesores (idProfesor,cuilProfesor, nombreProfesor, apellidoProfesor, correoProfesor,active) VALUES (NULL,'{}', '{}', '{}','{}',1)".format(cuilProfesor, nombreProfesor, apellidoProfesor,correoProfesor)
            # ultimoId = len(self.__class__.lista)
            # self.__class__.lista.append( Alumno(str(ultimoId), alumnCompleto))
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise
    
    def buscar_listaprofesor(self,active = 1):
        sql="SELECT * FROM profesores WHERE active = '{}' ORDER BY nombreProfesor ASC".format(active)
        
        try:
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        except Exception as e:
            raise
    
    def actualizar_profesor(self,cuilProfe, nombreProfe, apellidoProfe,correoProfe,idProfesor):
        sql="UPDATE profesores SET cuilProfesor = '{}', nombreProfesor = '{}', apellidoProfesor = '{}', correoProfesor = '{}' WHERE idProfesor = '{}'".format(cuilProfe, nombreProfe, apellidoProfe,correoProfe,idProfesor)

        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise

    def baja_profesor(self,idProfesor,active = 0):
        sql="UPDATE profesores SET active = '{}' WHERE idProfesor = '{}'".format(active,idProfesor)
        
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise
