from pydantic import BaseModel
from typing import Annotated, Optional
from fastapi import Form


class Contact(BaseModel):
    name: Annotated[str, Form()]
    email: Annotated[str, Form()]
    subject: Annotated[str, Form()]
    message: Annotated[str, Form()]



class Response(BaseModel):
    message: Optional [str] = None
    data : Optional [str | list | dict] = None