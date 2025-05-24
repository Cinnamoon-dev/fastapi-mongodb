import os
from pymongo import MongoClient

MONGO_CLIENT = os.getenv("MONGO_CLIENT", "mongodb://localhost:27017")

client = MongoClient(MONGO_CLIENT)
db = client.college
users_collection = db["users"]
user_types_collection = db["user_types"]

def test_mongo_conn():
    try:
        client.admin.command('ping')
        print(f"ping {MONGO_CLIENT}")
    except Exception as e:
        print(e)