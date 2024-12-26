from fastapi import APIRouter
from app.models.studentModel import Student
from app.adapters.studentAdapter import StudentAdapter
from app.schemas.studentSchemas import StudentEditSchema

router = APIRouter(prefix="/student")


@router.get("/all")
async def student_all():
    return StudentAdapter().student_all_controller()

@router.get("/view/{id}")
async def student_view(id):
    return StudentAdapter().student_view_controller(id)

@router.post("/add")
async def student_add(student: Student):
    return StudentAdapter().student_add_controller(student)

@router.put("/edit/{id}")
async def student_edit(id: str, student: StudentEditSchema):
    return StudentAdapter().student_edit_controller(id, student)

@router.delete("/delete/{id}")
async def student_delete(id: str):
    return StudentAdapter().student_delete_controller(id)