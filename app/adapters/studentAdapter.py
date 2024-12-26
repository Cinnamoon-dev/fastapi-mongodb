from app.models.studentModel import Student
from app.services.studentServices import StudentService

class StudentAdapter:
    def student_all_controller(self):
        students = StudentService().get_all_students()
        return {"error": False, "data": students}
    
    def student_view_controller(self, id):
        student = StudentService().view_one_student(id)
        return {"error": False, "data": student}
    
    def student_add_controller(self, student: Student):
        inserterd_id = StudentService().add_student(student)
        return {"error": False, "message": f"Student {inserterd_id} added successfully"}
    
    def student_edit_controller(self, id, fields):
        edited_id = StudentService().edit_student(id, fields)
        return {"error": False, "message": f"Student {edited_id} edited successfully"}
    
    def student_delete_controller(self, id):
        deleted_id = StudentService().delete_student(id)
        return {"error": False, "message": f"Student {deleted_id} deleted successfully"}