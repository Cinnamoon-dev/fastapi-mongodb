from bson import ObjectId
from fastapi import APIRouter
from app.database import students_collection
from app.models.studentModel import Student, student_serial, list_students

router = APIRouter(prefix="/student")


@router.get("/all")
async def student_all():
    students = list_students(students_collection.find())
    return {"error": False, "data": students}

@router.get("/view/{id}")
async def student_view(id):
    student = students_collection.find_one({"_id": ObjectId(id)})

    if not student:
        return {"error": True, "message": "Student not found"}

    return {"error": False, "data": student_serial(student)}

@router.post("/add")
async def student_add(student: Student):
    inserted_student_result = students_collection.insert_one(dict(student))
    return {"error": False, "message": f"Student {str(inserted_student_result.inserted_id)} added successfully"}

@router.put("/edit/{id}")
async def student_edit(id: str, student: Student):
    students_collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(student)})
    return {"error": False, "message": "Student updated successfully"}

@router.delete("/delete/{id}")
async def student_delete(id: str):
    students_collection.find_one_and_delete({"_id": ObjectId(id)})
    return {"error": False, "message": "Student deleted successfully"}