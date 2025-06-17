import os
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_CLIENT = os.getenv("MONGO_CLIENT", "mongodb://localhost:27017")

client = AsyncIOMotorClient(MONGO_CLIENT)
db = client.college
users_collection = db["users"]
user_types_collection = db["user_types"]


async def test_mongo_conn():
    try:
        await client.admin.command("ping")
        print(f"ping {MONGO_CLIENT}")
    except Exception as e:
        print(e)
