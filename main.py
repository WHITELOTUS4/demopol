from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
import Preprocessor
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

def timeStamp():
   return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

@app.get("/")
def read_root():
    return {"Ahoy hoy": "Universe"}

@app.get("/api/")
def read_root(number: list[str] = Query(...)):
    return {"result": number, "time": timeStamp()}

class ImageData(BaseModel):
    form: str
    img: str

@app.post("/api/imageConverter")
def read_root(data: ImageData):
    src = Preprocessor.convert_jpg(data.img)
    return {"result": src, "time": timeStamp()}

@app.get("/sum")
def read_root(a, b):
    result = Preprocessor.sum(int(a), int(b))
    return {"sum": result, "time": timeStamp()}

