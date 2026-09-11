from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class TestModel(BaseModel):
    id: int
    name: str
    email: str

@router.get("/test")
def test():
    return {"message": "Hello, FastAPI!"}