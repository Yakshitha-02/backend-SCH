from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    user_id: Optional[str]
    name: str
    email: str
    bio: str = None
    # profile_picture: str = None [Enhancement: Add profile picture field]
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

    