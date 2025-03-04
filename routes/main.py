from fastapi import APIRouter
from models.User import User

router = APIRouter()

@router.post("/")
def validate_user(user: User):
    return {"data": user.model_dump()}


@router.get("/")
def read_root():
    return {"message": "Hello World from main routes"}
