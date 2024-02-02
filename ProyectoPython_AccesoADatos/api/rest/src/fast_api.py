from fastapi import FastAPI, requests

app = FastAPI()

print("Hola como andas??")

@app.get("/")
def comprobar_conexion():
    return {"confirmation_message": "<i>Hemos conseguido establecer la conexión</i>"}

#Hacer un CRUD con FastAPI (o más o menos!!):

tasks = [{"name": "tarea1"}, {"name": "tarea2"}]

@app.route("/tasks")
def getAll():
    return {"tasks": tasks}
    #return tasks //Asi sería solo la lista

@app.route("/tasks", methods=["POST"])
def recive():
    try:
        data = requests.get_json()
        print(f"Data: {data}")
        return "200"
    except: return "-1"