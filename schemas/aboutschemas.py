from pydantic import BaseModel
from fastapi import File, UploadFile

class About(BaseModel):
    header : str
    body : str
