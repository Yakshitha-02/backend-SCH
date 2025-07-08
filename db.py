import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

# Load from .env locally; has no effect on Railway
load_dotenv()

DATABASE_URL = os.environ.get("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in environment variables!")

client = AsyncIOMotorClient(DATABASE_URL)
db = client["student_collaboration"]

comments_collection = db.comments
