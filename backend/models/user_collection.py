from typing import List
from pydantic import BaseModel

from backend.models.user import UserOutput

class UserCollection(BaseModel) :
    Users : List[UserOutput]