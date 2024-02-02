from abc import ABC, abstractmethod
from models.TODOs.TODO import TODO

class ICrudRepository(ABC):
    @abstractmethod
    def getAllTODOs(self) -> list[TODO]:
        pass

    @abstractmethod
    def getTODOById(self, id: int) -> TODO:
        pass

    @abstractmethod
    def saveTODOData(self, todo: TODO) -> bool:
        pass

    @abstractmethod
    def deleteTODO(self, id: int) -> bool:
        pass

    @abstractmethod
    def deleteAllTODOs(self) -> bool:
        pass