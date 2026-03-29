from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    name:str
    age:int

class UserUpdate(BaseModel):
    age: int

class UserPatch(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None