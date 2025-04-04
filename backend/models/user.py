from pydantic import BaseModel
from pydantic import EmailStr, Field

class User(BaseModel) :
    username : str
    password : str
    first_name : str
    last_name : str
    # email : EmailStr