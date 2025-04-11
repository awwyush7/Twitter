from passlib.context import CryptContext
from backend.services.password.IPasswordService import IPasswordService

class PasswordService(IPasswordService) :
    def __init__(self) :
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        self.pwd_context.update(schemes=["bcrypt"], deprecated="auto")
    
    def hash_password(self,password: str) -> str:
        return self.pwd_context.hash(password)

    # Function to verify a password
    def verify_password(self,plain_password: str, hashed_password: str) -> bool:
        return self.pwd_context.verify(plain_password, hashed_password)