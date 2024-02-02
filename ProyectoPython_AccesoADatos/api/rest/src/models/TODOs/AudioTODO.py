from models.TODOs.TiposTODO import TiposTODO
from models.TODOs.IValorTODO import IValorTODO
from datetime import datetime

class AudioTODO(IValorTODO):
    def __init__(self, id: int, fechaCreacion: str, isChecked: bool, valor: str):
        self._id = id
        self._fechaCreacion = fechaCreacion
        self._isChecked = isChecked
        self._valor = valor
        self._tipo = TiposTODO.AUDIO.name

    @property
    def id(self) -> str:
        return self._id
    
    @id.setter
    def id(self, value: str) -> None:
        self._id = value    

    @property
    def fechaCreacion(self) -> datetime:
        return self._fechaCreacion
    
    @fechaCreacion.setter
    def fechaCreacion(self, value: datetime) -> None:
        self._fechaCreacion = value

    @property
    def isChecked(self) -> bool:
        return self._isChecked
    
    @isChecked.setter
    def isChecked(self, value: bool) -> None:
        self._isChecked = value

    @property
    def valor(self) -> str:
        return self._valor
    
    @valor.setter
    def valor(self, value: str) -> None:
        self._valor = value