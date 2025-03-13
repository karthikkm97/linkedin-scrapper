from pydantic import BaseModel
from typing import List, Optional

class Post(BaseModel):
    post_id: str
    content: str
    comments: List[str]
    likes: int
    timestamp: str

class Page(BaseModel):
    page_id: str
    name: str
    url: str
    profile_picture: str
    description: str
    website: str
    industry: str
    followers: int
    head_count: int
    specialities: List[str]
    posts: List[Post]