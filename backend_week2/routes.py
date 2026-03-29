from fastapi import APIRouter, HTTPException
from services import create_user, DuplicateEmailError
from schemas import UserCreate, UserRead

router = APIRouter()

@router.post("/users", response_model=UserRead)
def create_user_endpoint(user: UserCreate):
    try:
        created_user= create_user(name= user.name, email=user.email)
        return created_user
    
    except DuplicateEmailError:
        raise HTTPException(
            status_code=409,
            detail="User already exists"
        )

