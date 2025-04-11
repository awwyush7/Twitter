from backend.models.user import UserInput, UserOutput
from backend.services.db_services.user_db.IUserServiceDB import IUserServiceDB
from backend.services.user.IUserService import IUserService

class UserService(IUserService) :
    # Managment of users
    def __init__(self,db_Service : IUserServiceDB) :
        self.db_service = db_Service
    
    async def add(self,user : UserInput) :
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
    
    def get_current_user(self) -> UserOutput:
        user = UserOutput(username="awwyush",first_name="Ayush",last_name="Pandey")
        return user