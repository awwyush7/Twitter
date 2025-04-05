from backend.models.user import User
from passlib.context import CryptContext
from motor.motor_asyncio import AsyncIOMotorClient

from backend.services.password_managment import PasswordManagment
from backend.services.user_service_db import UserServiceDB

class UserService() :
    # Managment of users
    def __init__(self) :
        self.db_service = UserServiceDB()
        self.password_manager = PasswordManagment()
    
    async def add(self,user : User) :
        db_service = self.db_service
        return await db_service.add(user)
    
    async def get_all(self) : 
        db_service = self.db_service
        users = await db_service.get_all()
        print(type(users))
        return users
    
    async def get_user(self,username) -> dict :
        db_service = self.db_service
        return await db_service.get_user(username)
    
    async def delete_database(self) :
        db_service = self.db_service
        return await db_service.delete_database()