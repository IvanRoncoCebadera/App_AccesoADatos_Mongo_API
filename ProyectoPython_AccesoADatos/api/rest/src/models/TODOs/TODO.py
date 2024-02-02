from dataclasses import dataclass
from datetime import datetime
from models.TODOs.TiposTODO import TiposTODO


@dataclass
class TODO:
    _id: int
    _fechaCreacion: datetime
    _isChecked: bool
    _tipo: str = TiposTODO.NULL.name