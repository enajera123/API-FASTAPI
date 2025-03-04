from fastapi import APIRouter
from models.User import User

router = APIRouter()

@router.post("/users")
def validate_user(user: User):
    if(len(user.password) > 8):
        return {"data": user.model_dump()}
    return {"data": "Password must be at least 8 characters long"}


@router.get("/users")
def read_root():
    return {"message": "Hello World from user routes"}
