from typing import List
from fastapi.datastructures import Default
from pydantic import BaseModel

class UserProperties(BaseModel) :
    user_id : int
    username : str
    bio : str = Default("")
    followers : List[str]
    following : List[str]
    total_followers : int
    total_following : int
