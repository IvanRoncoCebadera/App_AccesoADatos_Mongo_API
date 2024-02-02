from pymongo import MongoClient

client = MongoClient("mongodb://root:example@localhost:27017") #Con la conexión así me puedo conectar desde local without problems
print('OK')
db = client.testdb
print('OK')

try: 
    breakpoint(db.command("serverStatus")) #De esta forma, uso los breakpoints de pdb - Python Debugger
except Exception as e: print(e)
else: print("You are connected!")