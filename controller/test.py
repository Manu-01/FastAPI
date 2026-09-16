from fastapi import APIRouter, HTTPException,status
from pydantic import BaseModel

router = APIRouter(
    prefix="/test",    
    tags=["Test"]
)

@router.get("/list")
def test():
    return {
        "data": "Test API is working fine",
        "message": "Test API is working fine",
        "isSuccess": True
    }
