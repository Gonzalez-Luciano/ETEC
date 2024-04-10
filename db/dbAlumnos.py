import pymysql
from db.DataBase import DataBase
import cryptography

class dbAlumnos(DataBase):
    def __init__(self,hostdb,userdb,db,password):
        super().__init__(hostdb,userdb,db,password)

    def crear_alumno(self,cuilAlumn,nombreAlumn,apellidoAlumn):
        sql="INSERT INTO alumnos (idAlumno,cuilAlumno, nombreAlumno, apellidoAlumno,active) VALUES (NULL,'{}', '{}', '{}','1')".format(cuilAlumn, nombreAlumn, apellidoAlumn)
            # ultimoId = len(self.__class__.lista)
            # self.__class__.lista.append( Alumno(str(ultimoId), alumnCompleto))
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise

    def buscar_listalumno(self,active = 1):
        sql="SELECT * FROM alumnos  WHERE active = '{}' ORDER BY nombreAlumno ASC".format(active)
        
        try:
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        except Exception as e:
            raise
        
    def actualizar_alumno(self,cuilAlumn, nombreAlumn, apellidoAlumn,idAlumno):
        sql="UPDATE alumnos SET cuilAlumno = '{}', nombreAlumno = '{}', apellidoAlumno = '{}' WHERE idAlumno = '{}'".format(cuilAlumn, nombreAlumn, apellidoAlumn,idAlumno)

        try:
            self.cursor.execute(sql)
            print(self.cursor)
            self.connection.commit()
        except Exception as e:
            raise
        
    def baja_alumno(self,idAlumno,active = 0):
        sql="UPDATE alumnos SET active = '{}' WHERE idAlumno = '{}'".format(active,idAlumno)
        
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise
        