from fastapi import APIRouter, HTTPException
from users.services import UserService
from common.users.service import UsersService
from common.users.schema import UserBase

router = APIRouter(prefix="/user")
users_service = UsersService()


@router.post("/user")
def create_user(name: str, email: str):
    return users_service.create(name, email)




@router.get("/user/{user_id}", response_model=UserBase)
def read_user(user_id: int):
    return users_service.find(user_id) or {}


@router.get("/users")
def read_all_users():
    return users_service.find_all()


@router.put("/user/{user_id}")
def update_user(user_id: int, name: str):
    return users_service.update(user_id, name) or {}


@router.delete("/user/{user_id}")
def delete_user(user_id: int):
    users_service.delete(user_id)
    return {"message": f"User with ID {user_id} deleted successfully"}

@router.get("/")
def read_root():
    return {"Hello": "World"}