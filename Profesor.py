from dataclasses import *

@dataclass
class Profesor():
    id: int
    cuil: int
    nombre: str
    apellido: str
    mail: str
    active: bool    
