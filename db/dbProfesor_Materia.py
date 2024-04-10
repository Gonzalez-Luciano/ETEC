import pymysql
from db.DataBase import DataBase
import cryptography

class dbProfesor_Materia(DataBase):
    def __init__(self,hostdb,userdb,db,password):
        super().__init__(hostdb,userdb,db,password)
        
    
    def agregarProfesor_Materia(self,idProfesor,idMateria,active=1):
        sql="INSERT INTO profesores_materias (idProfesores_materias,idProfesor, idMateria, active) VALUES (NULL,'{}', '{}', '{}')".format(idProfesor, idMateria, active)
            # ultimoId = len(self.__class__.lista)
            # self.__class__.lista.append( Alumno(str(ultimoId), alumnCompleto))
        try:
            if not self.existe(idProfesor,idMateria):
                self.cursor.execute(sql)
                self.connection.commit()
                return True 
            
            return False
        except Exception as e:
            raise
        
        
    def bajaProfesor_Materia(self,idProfesor,idMateria,active=0):
        sql="UPDATE profesores_materias SET active = '{}' WHERE idProfesor = '{}' AND idMateria = '{}'".format(active,idProfesor,idMateria)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            return True
        except Exception as e:
            raise
                
                
    def existe(self,idAlumno,idMateria):
        sql="SELECT COUNT(*) FROM profesores_materias WHERE idProfesor = '{}' AND idMateria = '{}' AND active = 1".format(idAlumno,idMateria)
            # ultimoId = len(self.__class__.lista)
            # self.__class__.lista.append( Alumno(str(ultimoId), alumnCompleto))
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchone()
            return True if result[0] else False
        except Exception as e:
            raise
    
    
    def bajaPorMateria(self,idMateria):
        sql="UPDATE profesores_materias SET active = '0' WHERE idMateria = '{}'".format(idMateria)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            return True
        except Exception as e:
            raise
    
    
    def mostrarMateria(self,idProfesor,active=1):
        sql= "SELECT m.* FROM profesores_materias pm INNER JOIN materias m ON m.idMateria = pm.idMateria INNER JOIN profesores p ON p.idProfesor = pm.idProfesor WHERE p.idProfesor = '{}' AND pm.active = '{}' ORDER BY m.nombreMateria ASC".format(idProfesor,active)
       
        try:
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        except Exception as e:
            raise     