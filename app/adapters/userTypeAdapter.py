from fastapi import HTTPException

from app.models.userTypeModel import UserType
from app.schemas.userTypeSchema import UserTypeAddSchema
from app.services.userTypeService import UserTypeService

class UserTypeAdapter:
    async def user_type_all_controller(self):
        user_types = await UserTypeService().get_all_user_types()
        return {"error": False, "data": user_types}
    
    async def user_type_view_controller(self, id):
        user_type = await UserTypeService().view_one_user_type(id)
        return {"error": False, "data": user_type}
    
    async def user_type_add_controller(self, user_type: UserTypeAddSchema):
        try:
            new_user_type = UserType(name=user_type.name)
        except Exception:
            raise HTTPException(status_code=422, detail="user_type body invalid!")

        inserted_id = await UserTypeService().add_user_type(new_user_type)
        return {"error": False, "message": f"user_type {inserted_id} added successfully"}
    
    async def user_type_edit_controller(self, id, fields):
        edited_id = await UserTypeService().edit_user_type(id, fields)
        return {"error": False, "message": f"user_type {edited_id} edited successfully"}
    
    async def user_type_delete_controller(self, id):
        deleted_id = await UserTypeService().delete_user_type(id)
        return {"error": False, "message": f"user_type {deleted_id} deleted successfully"}