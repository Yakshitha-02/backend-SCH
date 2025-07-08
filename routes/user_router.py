from uuid import uuid4
from fastapi import APIRouter, HTTPException
from models.user import User, UserCreate, UserLogin
from db import db
from utils import create_jwt_token, get_hashed_password, check_password

router = APIRouter()

@router.post("/sign-up", response_model=dict)
async def create_user(user: UserCreate):
    user_exists = await db.users.count_documents({"email": user.email}) > 0
    if user_exists:
        raise HTTPException(status_code=400, detail="User with this email already exists")

    new_user = User(
        user_id=str(uuid4()),
        name=user.name,
        email=user.email,
        password=get_hashed_password(user.password),
        bio=user.bio
    )

    await db.users.insert_one(new_user.dict())

    return {
        "status": "success",
        "message": "User created successfully",
        "data": {
            "id": new_user.user_id,
            "email": new_user.email
        }
    }


@router.post("/login", response_model=dict)
async def login_user(payload: UserLogin):
    user = await db.users.find_one({"email": payload.email})
    if not user:
        raise HTTPException(status_code=404, detail="User not found! Please sign up first.")

    if not check_password(user['password'], payload.password):
        raise HTTPException(status_code=401, detail="Invalid password")

    token = create_jwt_token({"email": user['email']})

    return {
        "status": "success",
        "message": "Login successful",
        "data": {
            "id": user.get('user_id') or str(user['_id']),
            "email": user['email'],
            "token": token
        }
    }

@router.get("/", response_model=dict)
async def get_users():
    users = await db.users.find({}, {"_id": 0}).to_list(length=100)
    return {
        "status": "success",
        "message": "User information retrieved successfully",
        "data": users
    }
