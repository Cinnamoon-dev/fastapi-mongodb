import os
from pymongo import MongoClient

client = MongoClient(os.getenv("MONGO_CLIENT", "mongodb://localhost:27017"))
db = client.college
students_collection = db["students"]

def test_mongo_conn():
    try:
        client.admin.command('ping')
        print("ping db")
    except Exception as e:
        print(e)