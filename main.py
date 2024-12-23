from bson import ObjectId
import os, uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from pymongo.mongo_client import MongoClient

app = FastAPI(title="A simple test with MongoDB")
client = MongoClient(os.getenv("MONGO_CLIENT", "mongodb://localhost:27017"))
db = client.college
students_collection = db["students"]

def test_mongo_conn():
    try:
        client.admin.command('ping')
        print("ping db")
    except Exception as e:
        print(e)

class Student(BaseModel):
    name: str
    age: int
    course: str

def student_serial(student: Student):
    return {
        "id": str(student["_id"]),
        "name": student["name"],
        "age": student["age"],
        "course": student["course"]
    }

def list_students(students):
    return [student_serial(student) for student in students]

@app.get("/")
def main():
    return {"message": "Hello, World!"}

@app.get("/student/all")
async def student_all():
    students = list_students(students_collection.find())
    return {"error": False, "data": students}

@app.get("/student/view/{id:int}")
async def student_view(id: int):
    student = students_collection.find_one(id)

    if not student:
        return {"error": True, "message": "Student not found"}

    return {"error": False, "data": student_serial(student)}

@app.post("/student/add")
async def student_add(student: Student):
    result = students_collection.insert_one(dict(student))
    return {"error": False, "message": "Student added successfully"}

@app.put("/student/edit/{id}")
async def student_edit(id: str, student: Student):
    students_collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(student)})
    return {"error": False, "message": "Student updated successfully"}

@app.delete("/student/delete/{id}")
async def student_delete(id: str):
    students_collection.find_one_and_delete({"_id": ObjectId(id)})
    return {"error": False, "message": "Student deleted successfully"}


if __name__ == '__main__':
    test_mongo_conn()
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)