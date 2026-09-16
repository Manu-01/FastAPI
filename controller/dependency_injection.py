from fastapi import Depends,HTTPException,status,APIRouter

router = APIRouter(
    prefix="/dependency_injection",
    tags=["DI"]
)
def common_message():
    return {"message": "This is a common message from dependency injection"}


@router.get("/list")
def get_list(data = Depends(common_message)):
    return data

