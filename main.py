from fastapi import FastAPI, status
from fastapi.exception_handlers import HTTPException
from pydantic import BaseModel
from typing import List, Optional
app = FastAPI()



@app.get('/')
async def start():
    return {"message": "Hello World"}

