from pydantic import BaseModel
from typing import Annotated, Optional
from fastapi import Form

class UserBase(BaseModel):
    username: Annotated[str, Form()]
    first_name: Annotated[str, Form()]
    last_name: Annotated[str, Form()]
    email: Annotated[str, Form()]
    password: Annotated[str, Form()]

class User(UserBase):
    User_id: str


class Response(BaseModel):
    message: Optional [str] = None
    data : Optional [str | list] = None