from dataclasses import dataclass
from models.TODOs.TiposTODO import TiposTODO
from models.TODOs.TODO import TODO

@dataclass
class SublistaTODO(TODO):
    _lista: list[TODO]
    _tipo: TiposTODO = TiposTODO.SUBLISTA.name