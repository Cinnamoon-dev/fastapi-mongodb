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
        # extract in a method
        document_to_update = students_collection.find_one({"_id": ObjectId(id)})

        if not document_to_update:
            raise HTTPException(status_code=404, detail=f"student {id} not found")

        document_to_update = student_serial(document_to_update)

        fields_dict = dict(fields)
        keys = []

        for k in fields_dict.keys():
            if not fields_dict[k]:
                keys.append(k)
        
        for key in keys:
            fields_dict.pop(key)

        print(fields_dict)

        for k, v in fields_dict.items():
            document_to_update[k] = v
            print(document_to_update)

        print(document_to_update)

        edited_document = students_collection.update_one({"_id": ObjectId(id)}, {"$set": document_to_update})
        return edited_document.upserted_id
    
    def delete_student(self, id):
        # TODO
        # show when not found
        deleted_document = students_collection.find_one_and_delete({"_id": ObjectId(id)})
        return dict(deleted_document)["_id"]