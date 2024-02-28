from typing import Union
from datetime import date
from datetime import datetime
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/datetime")
def date_time():
    dt= datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"Data | Hora ": dt}

@app.get("/sub")
def subtract(a: Union[str, None] = None, b: Union[str, None] = None):
    sub = int(a) - int(b)
    return {"Subtração: ": sub}

@app.get("/add")
def add(a: Union[str, None] = None, b: Union[str, None] = None):
    soma = int(a) + int(b)
    return {"Soma: ": soma}

@app.get("/div")
def divide(a: Union[str, None] = None, b: Union[str, None] = None):
    div = int(a) / int(b)
    return {"Divisão: ": div}

@app.get("/mult")
def multiply(a: Union[str, None] = None, b: Union[str, None] = None):
    mult = int(a) * int(b)
    return {"Multiplicação: ": mult}