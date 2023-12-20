from pymongo import MongoClient;

print("Hello world!!!")

client = MongoClient("mongo_db://root:example@mongo:27017")
db = client.testDb

try: db.command("serverStatus")
except Exception as e: print(e)
else: print("You are conected")

client.close()