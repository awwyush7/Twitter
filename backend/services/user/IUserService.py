from abc import ABC, abstractmethod

class IUserService(ABC):
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
    def get_current_user(self) :
        pass
