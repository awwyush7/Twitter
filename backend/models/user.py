from pydantic import BaseModel
from pydantic import EmailStr, Field

class UserInput(BaseModel) :
    username : str
    password : str
    first_name : str
    last_name : str
    # email : EmailStr

class UserOutput(BaseModel) :
    user_id : int
    username : str
    first_name : str
    last_name : str
    # email : EmailStr
