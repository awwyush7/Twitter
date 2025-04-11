from pydantic import BaseModel
from pydantic import EmailStr, Field

class Tweet(BaseModel) :
    id : int = Field(..., title="Tweet ID", description="Unique identifier for the tweet")
    user_id : int = Field(..., title="User ID", description="ID of the user who posted the tweet")
    likes : int = Field(..., title="Likes", description="Number of likes the tweet has received")
    content : str = Field(..., title="Tweet Content", description="Content of the tweet")
    created_at : str = Field(..., title="Creation Time", description="Time when the tweet was created")
    updated_at : str = Field(..., title="Update Time", description="Time when the tweet was last updated") 
    