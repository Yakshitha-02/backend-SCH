from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    bio: Optional[str] = None

class User(BaseModel):
    user_id: Optional[str]
    name: str
    email: str
    password: str
    bio: Optional[str] = None

class UserLogin(BaseModel):
    email: str
    password: str
