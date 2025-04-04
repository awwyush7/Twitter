from typing import List
from pydantic import BaseModel
from pydantic import EmailStr, Field

from backend.models.user import User

class UserCollection(BaseModel) :
    Users : List[User]