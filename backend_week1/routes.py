from fastapi import APIRouter, HTTPException
from models import User
from models import UserUpdate
from models import UserPatch

router = APIRouter()
users_db = []

@router.post("/users")
def create_user(user: User):
    for existing_user in users_db:
        if existing_user.name == user.name:
            raise HTTPException(
                status_code=400,
                detail="User already exists"
            )
        
    users_db.append(user)
    return {
        "message": f"User {user.name} created",
        "total_users": len(users_db)
    }

@router.get("/users")
def list_users():
    return users_db

@router.get("/users/{user_name}")
def get_user(user_name: str):
    for user in users_db:
        if user.name ==user_name:
            return user
        
    raise HTTPException(
        status_code=404,
        detail="User not found"
    )

@router.put("/users/{user_name}")
def update_user(user_name: str, update: UserUpdate):
    for user in users_db:
        if user.name==user_name:
            user.age=update.age
            return{
                "message": f"User {user.name} updated",
                "new_age": user.age
            }
    raise HTTPException(
        status_code=404,
        detail="User not found"
    )    

@router.delete("/users/{user_name}")
def delete_user(user_name: str):
    for index, user in enumerate(users_db):
        if user.name==user_name:
            users_db.pop(index)
            return {
                "message": f"User {user_name} deleted",
                "total_users": len(users_db)
            }
    raise HTTPException(
        status_code=404,
        detail="User not found"
    )

@router.patch("/users/{user_name}")
def patch_user(user_name: str, patch: UserPatch):
    for user in users_db:
        if user.name==user_name:
            if patch.name is not None:
                user.name=patch.name
            if patch.age is not None:
                user.age=patch.age

            return {
                "message": f"User {user_name} updated partially",
                "user": user
            }            

    raise HTTPException(
        status_code=404,
        detail="User not found"
    )

# @app.get("/health")
# def health():
#     return {"status": "ok"}

# @app.get("/hello")
# def hello():
#     return {"message": "Hello from my backend"}

# @app.get("/greet")
# def greet(name: int):
#     return {"message": f"Hello {name}"}
