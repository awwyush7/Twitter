from datetime import datetime, timedelta, timezone
import jwt
import os
from backend.services.password_managment import PasswordManagment
from backend.models.token import Token
from dotenv import load_dotenv, find_dotenv

from backend.services.user_service import UserService

load_dotenv(find_dotenv())

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES  = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES ")

class LoginService() :
# loading all the users and seraching through it or searching directly in the db with out loading the whole users.
    def __init__(self):
        self.password_managment =  PasswordManagment()
        self.user_service = UserService()
        
    async def get_user(self,user_login) :
        fetched_user = await self.user_service.get_user(user_login.username)
        print(fetched_user)
        return fetched_user
    
    async def verify_user(self,user_login) :
        fetched_user = await self.get_user(user_login)
        if(fetched_user == None) :
            return False
        try: 
            verify_pass = self.password_managment.verify_password(user_login.password, fetched_user["password"])
            return True
        except Exception as e:
            print(f"An error occurred during password verification: {e}")
            return False
            
    def create_access_token(self,data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=30))  # ✅ Use timezone-aware datetime
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    
    async def get_token(self,user_login) :
        verified = await self.verify_user(user_login)
        if(verified) :
            user = await self.user_service.get_user(user_login.username) 
            token = self.create_access_token(user,ACCESS_TOKEN_EXPIRE_MINUTES)
            return Token(access_token=token, token_type="bearer")
        else :
            return "No such user"