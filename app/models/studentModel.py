from pydantic import BaseModel

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