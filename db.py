from motor.motor_asyncio import AsyncIOMotorClient
from env import DATABASE_URL

client = AsyncIOMotorClient(DATABASE_URL)

db = client["student_collaboration"]