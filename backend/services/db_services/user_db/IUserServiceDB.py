from abc import ABC, abstractmethod

class IUserServiceDB(ABC):
    @abstractmethod
    async def add(self,user):
        pass
    @abstractmethod
    async def get_all(self) :
        pass
    @abstractmethod
    async def get_user(self,username):
        pass
    @abstractmethod
    async def delete_database(self) :
        pass
    @abstractmethod
    def serialize_user(self,user) :
        pass
    @abstractmethod
    def get_hashed_password(self,password) :
        pass
