from typing import Union
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def read_root():
    return {"Hello": "We Love Datascientest, and we did it. We built a CI/CD Pipeline !! modif at 16:44"}
