
class Profesor():

    NombreUsuario = ""
    Contrasena = ""
    Materia= ""

    def __init__(self, nombreUsuario, contrasena, materia):
        self.NombreUsuario = nombreUsuario
        self.Contrasena = contrasena
        self.Materia = materia

    def GetNombreUsuario(self):
        return self.NombreUsuario

    def GetContrasena(self):
        return self.Contrasena

    def GetMateria(self):
        return self.Materia

    def  SetNombreUsuario(self,idalumno):
        self.NombreUsuario= idalumno  
    
    def  SetContrasena(self,nombre):
        self.Contrasena= nombre 

    def  SetMateria(self,turno):
        self.Materia= turno  

    def MostrarProfesor(self):
        return  "Usuario: " + self.NombreUsuario + ", Contraseña: " + self.Contrasena + ", Materia: " + self.Materia