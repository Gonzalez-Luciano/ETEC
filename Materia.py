from dataclasses import *
import inspect

@dataclass
class Materia():
    id: int
    nombre: str
    descripcion: str
    active: bool    