from dataclasses import *

@dataclass
class Alumno():
    id: int
    cuil: int
    nombre: str
    apellido: str
    active: bool    

    def MostrarAlumno(self):
        return  f"Id: {self.id}\nUsuario: {self.nombre} {self.apellido}\nCuil:{self.cuil}\nActivo: {self.active} "

        

