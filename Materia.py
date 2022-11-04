from dataclasses import *
import inspect

@dataclass
class Materia():
    id: int
    nombre: str
    descripcion: str
    active: bool    

    def MostrarMateria(self):
        return  f"Id: {self.id}\nNombre: {self.nombre}\nDescripción: {self.descripcion}\nActivo: {self.active} "
    