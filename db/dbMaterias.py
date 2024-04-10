import pymysql
from db.DataBase import DataBase
import cryptography

class dbMaterias(DataBase):
    def __init__(self,hostdb,userdb,db,password):
        super().__init__(hostdb,userdb,db,password)

    def crear_materia(self,nombreMateria,descripMateria):
        sql="INSERT INTO materias (idMateria, nombreMateria, descripcionMateria,active) VALUES (NULL, '{}', '{}',1)".format(nombreMateria, descripMateria)
                # ultimoId = len(self.__class__.lista)
                # self.__class__.lista.append( Alumno(str(ultimoId), alumnCompleto))
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise
    
    
    def buscar_listamateria(self,active = 1):
        sql="SELECT * FROM materias  WHERE active = '{}' ORDER BY nombreMateria ASC".format(active)
        
        try:
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        except Exception as e:
            raise
    
    
    def actualizar_materia(self,nombreMateria, descripMateria,idMateria):
        sql="UPDATE materias SET nombreMateria = '{}', descripcionMateria = '{}' WHERE idMateria = '{}'".format(nombreMateria, descripMateria, idMateria)

        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise
        
        
    def baja_materia(self,idMateria,active = 0):
        sql="UPDATE materias SET active = '{}' WHERE idMateria = '{}'".format(active,idMateria)
        
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise
            