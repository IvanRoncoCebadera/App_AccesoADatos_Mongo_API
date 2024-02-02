from abc import ABC, abstractmethod
from datetime import datetime

class IValorTODO(ABC):
    @property
    @abstractmethod
    def id(self) -> int:
        pass

    @id.setter
    @abstractmethod
    def id(self, value: int) -> None:
        pass

    @property
    @abstractmethod
    def fechaCreacion(self) -> datetime:
        pass

    @fechaCreacion.setter
    @abstractmethod
    def fechaCreacion(self, value: datetime) -> None:
        pass

    @property
    @abstractmethod
    def isChecked(self) -> bool:
        pass

    @isChecked.setter
    @abstractmethod
    def isChecked(self, value: bool) -> None:
        pass  # Fix the method name here

    @property
    @abstractmethod
    def valor(self) -> str:
        pass

    @valor.setter
    @abstractmethod
    def valor(self, value: str) -> None:
        pass