from abc import ABC, abstractmethod

class IPasswordService(ABC):
    @abstractmethod
    def hash_password(self,password):
        pass
    @abstractmethod
    def verify_password(self,plain_password, hashed_password) :
        pass
