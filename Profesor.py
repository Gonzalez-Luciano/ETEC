from dataclasses import *

@dataclass
class Profesor():
    id: int
    cuil: int
    nombre: str
    apellido: str
    mail: str
    active: bool    

    def MostrarProfesor(self):
        return  f"Id: {self.id}\nUsuario: {self.nombre} {self.apellido}\nCuil:{self.cuil}\nMail: {self.mail}\nactivo: {self.active} "
    