from fastapi import HTTPException
from bson import ObjectId
from app.database import students_collection
from app.models.studentModel import Student, student_serial, list_students

class StudentService:
    def get_all_students(self):
        # TODO
        # pagination
        return list_students(students_collection.find())
    
    def view_one_student(self, id):
        student = students_collection.find_one({"_id": ObjectId(id)})

        if not student:
            raise HTTPException(status_code=404, detail=f"student {id} not found")
        
        return student_serial(student)
    
    def add_student(self, student: Student):
        # TODO
        # add not repeat test case
        inserted_student_result = students_collection.insert_one(dict(student))
        return inserted_student_result.inserted_id
    
    def edit_student(self, id, fields):
        # TODO
        # show when not found
        edited_document = students_collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(student)})
        return dict(edited_document)["_id"]
    
    def delete_student(self, id):
        # TODO
        # show when not found
        deleted_document = students_collection.find_one_and_delete({"_id": ObjectId(id)})
        return dict(deleted_document)["_id"]