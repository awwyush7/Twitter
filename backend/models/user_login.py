from pydantic import BaseModel
from pydantic import EmailStr, Field

class UserLogin(BaseModel) :
    username : str
    password : str