from pymongo import MongoClient
from models.TODOs.TODO import TODO
from repository.ICrudRepository import ICrudRepository

validator = {
    "$jsonSchema": {
      "bsonType": "object",
      "required": ["_id", "_fechaCreacion", "_isChecked", "_tipo"],
      "properties": {
        "_id": {
          "bsonType": "int",
          "description": "Debe ser un entero."
        },
        "_fechaCreacion": {
          "bsonType": "date",
          "description": "Debe ser una fecha."
        },
        "_isChecked": {
          "bsonType": "bool",
          "description": "Debe ser un booleano."
        },
        "_tipo": {
          "enum": ["TEXTO", "IMAGEN", "AUDIO", "SUBLISTA", "NULL"],
          "description": "Debe ser uno de: TEXTO, IMAGEN, AUDIO, SUBLISTA, NULL."
        },
        "_valor": {
          "bsonType": "string",
          "description": "Campo opcional, si existe, debe ser una cadena."
        },
        "_lista": {
          "bsonType": "array",
          "items": {
            "type": "object",
            "properties": {
                "_id": {
                    "bsonType": "int",
                    "description": "Debe ser un entero."
                },
                "_fechaCreacion": {
                    "bsonType": "date",
                    "description": "Debe ser una fecha."
                },
                "_isChecked": {
                    "bsonType": "bool",
                    "description": "Debe ser un booleano."
                }
            }
          },
          "description": "Campo opcional, si existe, debe ser una lista de TODOs."
        }
      }
    }
  }

class TODORepository(ICrudRepository):
    def __init__(self):
        self.db = MongoClient("mongodb://root:example@mongo:27017").testdb

        try: self.db.create_collection("lista_TODO", validator = validator)
        except: pass

    def getAllTODOs(self) -> list[TODO]:
        try: return list(self.db.lista_TODO.find())
        except: return []

    def getTODOById(self, id: int) -> TODO:
        try: return TODO(**self.db.lista_TODO.find_one({"_id":id}))
        except: return None

    def saveTODOData(self, todo: TODO) -> bool:
        if self.getTODOById(todo._id) is None:
            return self.insertTODO(todo)
        else:
            return self.updateTODO(todo)

    def insertTODO(self, todo: TODO) -> bool:
        try: self.db.lista_TODO.insert_one(todo.__dict__)
        except: return False
        else: return True

    def updateTODO(self, todo: TODO) -> bool:
        try: self.db.lista_TODO.update_one({"_id":todo._id}, {"$set":todo.__dict__})
        except: return False
        else: return True

    def deleteTODO(self, id: int) -> bool:
        try: self.db.lista_TODO.delete_one({"_id":id})
        except: return False
        else: return True

    def deleteAllTODOs(self) -> bool:
        try: self.db.lista_TODO.delete_many({})
        except: return False
        else: return True