from typing import Any
from bson import ObjectId
from bson.errors import InvalidId
from fastapi import HTTPException
from pymongo.collection import UpdateResult

from . import document_update
from app.models.userTypeModel import UserType
from app.database import user_types_collection
from app.database.serializers import document_serial, list_documents


class UserTypeService:
    async def get_all_user_types(self) -> list[dict[str, Any]]:
        # TODO
        # pagination
        user_types = await user_types_collection.find().to_list()
        return list_documents(user_types)

    async def view_one_user_type(self, id: str) -> dict[str, Any]:
        user = await user_types_collection.find_one({"_id": ObjectId(id)})

        if not user:
            raise HTTPException(status_code=404, detail=f"user {id} not found")

        return document_serial(user)

    async def view_one_user_type_by_name(self, name: str) -> dict[str, Any]:
        user = await user_types_collection.find_one({"name": name})

        if not user:
            raise HTTPException(status_code=404, detail=f"user {name} not found")

        return document_serial(user)

    async def add_user_type(self, user_type: UserType) -> str:
        """Adiciona um usuário na base de dados e retorna seu id."""
        user_type_exists = await user_types_collection.find_one(
            {"name": user_type.name}
        )

        if user_type_exists:
            raise HTTPException(
                status_code=422,
                detail=f"user type with name {user_type.name} already exists",
            )

        inserted_user_result = await user_types_collection.insert_one(
            user_type.model_dump()
        )
        return inserted_user_result.inserted_id

    async def edit_user_type(self, id: str, fields: dict[str, Any]) -> UpdateResult:
        document_to_update = await user_types_collection.find_one({"_id": ObjectId(id)})

        if not document_to_update:
            raise HTTPException(status_code=404, detail=f"user {id} not found")

        document_update(document_to_update, fields)

        existing_document = await user_types_collection.find_one(
            {"name": fields.get("name")}
        )
        if existing_document:
            raise HTTPException(
                status_code=422,
                detail=f"user type with name {fields.get('name')} already exists",
            )

        update_result = await user_types_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": document_to_update}
        )
        return update_result

    async def delete_user_type(self, id: str) -> str:
        """Deleta um document na base de dados e retorna seu id."""
        try:
            deleted_document = await user_types_collection.find_one_and_delete(
                {"_id": ObjectId(id)}
            )
        except InvalidId:
            raise HTTPException(status_code=422, detail=f"id {id} invalid")
        except Exception:
            raise HTTPException(status_code=500, detail=f"Database Error")

        if deleted_document is None:
            raise HTTPException(status_code=404, detail=f"user {id} not found")

        return dict(deleted_document)["_id"]
