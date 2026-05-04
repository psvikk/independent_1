from fastapi import FastAPI
from pydantic import BaseModel
import random
import platform

app = FastAPI()

class NameRequest(BaseModel):
    name: str

@app.get("/api/status")
def status():
    return {"status": "Статус API работает"}

@app.get("/api/pc")
def get_pc():
    pc_info = {
        "операционная_система": platform.system(),
        "версия": platform.version(),
        "архитектура": platform.architecture(),
        "имя_компьютера": platform.node()
    }
    return pc_info

@app.get("/api/random-number")
def get_random():
    random_number = random.randint(1, 100)
    return {"number": random_number}

@app.post("/api/sayhello")
def say_hello(name_request: NameRequest):
    return {"message": f"Привет, {name_request.name}"}