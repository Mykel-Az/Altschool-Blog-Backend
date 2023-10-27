from pydantic import BaseModel
from datetime import datetime
from typing import Annotated, Optional
from fastapi import Body
from uuid import UUID

class Blog(BaseModel):
    blog_id : str
    user_id: str
    title: str
    first_name: str
    last_name: str
    blog_post : str
    time: datetime


class CreateBlog(BaseModel):
    title : str
    blog_post : str
    time: datetime
    

class BlogUpdate(BaseModel):
    title: str
    blog_post: str
    time: datetime

class Response(BaseModel):
    message: Optional [str] = None
    data : Optional [str | dict | list] = None


