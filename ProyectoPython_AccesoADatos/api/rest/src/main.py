#from pymongo import MongoClient
from models.TODOs.TextoTODO import TextoTODO
from models.TODOs.TiposTODO import TiposTODO
from models.TODOs.TODO import TODO
from datetime import datetime
from repository.ICrudRepository import ICrudRepository
from repository.TODORepository import TODORepository

print('Hello World!')

#client = MongoClient("mongodb://root:example@localhost:27017")
#print('OK')
#db = client.testdb
#print('OK')

nota: TODO = TODO(1, datetime.now(), False, TiposTODO.NULL.name)

notaTexto = TextoTODO(2, datetime.now(), True, "Hola wey!!")

repo: ICrudRepository = TODORepository()

repo.deleteAllTODOs()

repo.saveTODOData(nota)

repo.saveTODOData(notaTexto)

foundTodo = repo.getTODOById(nota._id)
print(foundTodo)

print("La lista de notas:")
todos = repo.getAllTODOs()
for todo in todos:
    print(todo)

nota = TODO(1, datetime.now(), False)

repo.saveTODOData(nota)

print("La lista de notas:")
todos = repo.getAllTODOs()

for todo in todos:
    print(todo)


#print(db)

#try: db.create_collection("TODOs")
#except Exception as e: print(e)
#else: print("Collection created succesfully")

#todos_collection = db['TODOs']

#try: todos_collection.insert_one(nota.__dict__)
#except Exception as e: print(e)
#else: print("TODO inserted succesfully!")

nuevaNota: TODO

#try: nuevaNota = todos_collection.find_one()
#except Exception as e: print(e)
#else: print(nuevaNota)

#Mañana hacer el repo del CRUD de un TODO, ver que funciona y punto. Después, empezar con interfaces!!!

#categorias_collection.insert_one({nombre:"Javi", prioridad:"2", notasConValor:[], notasConSublista:[]}) #Hacer esto pero de TODOs y punto, nada de complicarme demasiado

#try: db.command("show collections")
#except Exception as e: print(e)
#else: print("You are connected!")

#print('docker compose up --force-recreate') #Hacer esto pa iniciar el contenedor!!

#client.close()