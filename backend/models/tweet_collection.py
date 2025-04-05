from typing import List
from pydantic import BaseModel

from backend.models.tweet import Tweet


class TweetCollection(BaseModel) :
    Users : List[Tweet]