from abc import ABC, abstractmethod
from datetime import timedelta

class ILoginService(ABC):
    @abstractmethod
    async def get_user(self,user_login) :
        pass
    @abstractmethod
    async def verify_user(self,user_login):
        pass
    @abstractmethod
    def create_access_token(self,data: dict, expires_delta: timedelta | None = None) :
        pass
    @abstractmethod
    async def get_token(self,user_login) :
        pass