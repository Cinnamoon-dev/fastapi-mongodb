from typing import Any
from bson import ObjectId
from fastapi import HTTPException

from . import document_update
from app.models.userModel import User
from app.database import users_collection
from app.database.serializers import document_serial, list_documents

class UserService:
    async def get_all_users(self) -> list[dict[str, Any]]:
        # TODO
        # pagination
        return await self._get_all_users_with_type_name()
    
    async def view_one_user(self, id: str) -> dict[str, Any]:
        user = await users_collection.find_one({"_id": ObjectId(id)})

        if not user:
            raise HTTPException(status_code=404, detail=f"user {id} not found")
        
        return document_serial(user)
    
    async def add_user(self, user: User) -> str:
        # TODO
        # add not repeat test case
        new_user = user.model_dump()
        new_user["user_type_id"] = ObjectId(new_user["user_type_id"])
        
        inserted_user_result = await users_collection.insert_one(new_user)
        return inserted_user_result.inserted_id
    
    async def edit_user(self, id: str, fields: dict[str, Any]) -> str:
        document_to_update = await users_collection.find_one({"_id": ObjectId(id)})

        if not document_to_update:
            raise HTTPException(status_code=404, detail=f"user {id} not found")

        document_to_update = document_serial(document_to_update)
        document_update(document_to_update, fields)

        edited_document = await users_collection.update_one({"_id": ObjectId(id)}, {"$set": document_to_update})
        return edited_document.upserted_id
    
    async def delete_user(self, id: str) -> str:
        deleted_document = await users_collection.find_one_and_delete({"_id": ObjectId(id)})

        if deleted_document is None:
            raise HTTPException(status_code=404, detail=f"user {id} not found")

        return dict(deleted_document)["_id"]

    async def _get_all_users_with_type_name(self) -> list[dict[str, Any]]:
        """
            Função que retorna uma lista com todos os usuários do banco com o 
            nome do user_type ao invés do user_type_id. 
        """
        pipeline = [
            {
                "$lookup": {
                    "from": "user_types",
                    "localField": "user_type_id",
                    "foreignField": "_id",
                    "as": "user_type"
                }
            },
            {
                "$set": {
                    "user_type": {
                        "$arrayElemAt": ["$user_type.name", 0]
                    }
                }
            },
            {
                "$project": {
                    "user_type_id": 0
                }
            }
        ]

        users = await users_collection.aggregate(pipeline)
        users_list = await users.to_list()
        return list_documents(users_list)