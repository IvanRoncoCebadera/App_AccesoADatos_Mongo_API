from dataclasses import dataclass
from models.TODOs.IValorTODO import IValorTODO
from models.TODOs.SublistaTODO import SublistaTODO

@dataclass
class Categoria:
    nombre: str
    prioridad: int
    notasConValor: list[IValorTODO]
    notasConSublista: list[SublistaTODO]