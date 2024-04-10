import pymysql
from db.DataBase import DataBase
import cryptography

class dbAlumno_Materia(DataBase):
    def __init__(self,hostdb,userdb,db,password):
        super().__init__(hostdb,userdb,db,password)
        
    
    def agregarAlumno_Materia(self,idAlumno,idMateria,active=1):
        sql="INSERT INTO alumnos_materias (idAlumnos_materias,idAlumno, idMateria, active) VALUES (NULL,'{}', '{}', '{}')".format(idAlumno, idMateria, active)
            # ultimoId = len(self.__class__.lista)
            # self.__class__.lista.append( Alumno(str(ultimoId), alumnCompleto))
        try:
            if not self.existe(idAlumno,idMateria):
                self.cursor.execute(sql)
                self.connection.commit()
                return True 
            
            return False
        except Exception as e:
            raise
        
        
    def bajaAlumno_Materia(self,idAlumno,idMateria,active=0):
        sql="UPDATE alumnos_materias SET active = '{}' WHERE idAlumno = '{}' AND idMateria = '{}'".format(active,idAlumno,idMateria)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            return True
        except Exception as e:
            raise
                
                
    def existe(self,idAlumno,idMateria):
        sql="SELECT COUNT(*) FROM alumnos_materias WHERE idAlumno = '{}' AND idMateria = '{}' AND active = 1".format(idAlumno,idMateria)
            # ultimoId = len(self.__class__.lista)
            # self.__class__.lista.append( Alumno(str(ultimoId), alumnCompleto))
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchone()
            return True if result[0] else False
        except Exception as e:
            raise
    
    
    def bajaPorMateria(self,idMateria):
        sql="UPDATE alumnos_materias SET active = '0' WHERE idMateria = '{}'".format(idMateria)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            return True
        except Exception as e:
            raise
    
    
    def mostrarMateria(self,idAlumno,active=1):
        sql= "SELECT m.* FROM alumnos_materias am INNER JOIN materias m ON m.idMateria = am.idMateria INNER JOIN alumnos a ON a.idAlumno = am.idAlumno WHERE a.idAlumno = '{}' AND am.active = '{}' ORDER BY m.nombreMateria ASC".format(idAlumno,active)
       
        try:
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        except Exception as e:
            raise     



