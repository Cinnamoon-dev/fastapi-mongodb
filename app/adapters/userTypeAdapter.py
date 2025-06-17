from fastapi import HTTPException

from app.models.userTypeModel import UserType
from app.schemas.userTypeSchema import UserTypeAddSchema, UserTypeEditSchema
from app.services.userTypeService import UserTypeService


class UserTypeAdapter:
    async def user_type_all_controller(self):
        user_types = await UserTypeService().get_all_user_types()
        return {"error": False, "data": user_types}

    async def user_type_view_controller(self, id: str):
        user_type = await UserTypeService().view_one_user_type(id)
        return {"error": False, "data": user_type}

    async def user_type_view_by_name_controller(self, name: str):
        user_type = await UserTypeService().view_one_user_type_by_name(name)
        return {"error": False, "data": user_type}

    async def user_type_add_controller(self, user_type: UserTypeAddSchema):
        try:
            new_user_type = UserType(name=user_type.name)
        except Exception:
            raise HTTPException(status_code=422, detail="user_type body invalid!")

        inserted_id = await UserTypeService().add_user_type(new_user_type)
        return {
            "error": False,
            "message": "user_type added successfully",
            "id": inserted_id,
        }

    async def user_type_edit_controller(self, id: str, fields: UserTypeEditSchema):
        await UserTypeService().edit_user_type(id, fields.model_dump())
        return {"error": False, "message": "user_type edited successfully", "id": id}

    async def user_type_delete_controller(self, id: str):
        deleted_id = await UserTypeService().delete_user_type(id)
        return {
            "error": False,
            "message": "user_type deleted successfully",
            "id": deleted_id,
        }
