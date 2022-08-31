
class Alumno():

    IdAlumno = ""
    Nombre = ""
    Turno = ""

    def __init__(self, idAlumno, nombre, turno):
        self.IdAlumno = idAlumno
        self.Nombre = nombre
        self.Turno = turno

    def GetIdAlumno(self):
        return self.IdAlumno

    def GetNombre(self):
        return self.Nombre

    def GetTurno(self):
        return self.Turno

    def  SetIdAlumno(self,idalumno):
        self.IdAlumno= idalumno  
    
    def  SetNombre(self,nombre):
        self.Nombre= nombre 

    def  SetTurno(self,turno):
        self.Turno= turno  

    def MostrasAlumno(self):
        return  "Id: " + self.IdAlumno + ", Nombre: " + self.Nombre + ", Turno: " + self.Turno

    '''
    alumno = Alumno()
    alumno.SetIdAlumno("1")
    alumno.SetNombre("nombre")
    alumno.SetTurno("tarde")
    alumno2 = Alumno()
    alumno2.SetIdAlumno("2")
    alumno2.SetNombre("nombre2")
    alumno2.SetTurno("tarde2")

    

    listaAlumno = []
    listaAlumno.append(alumno)
    listaAlumno.append(alumno2)

    for alumno in listaAlumno: 
        print(alumno.MostrasAlumno())'''