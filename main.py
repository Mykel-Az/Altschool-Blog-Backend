from fastapi import FastAPI

from router.Home import router as Homeroute
from router.About import router as Aboutroute
from router.blog import router as Blogroute
from router.Contact import router as Contactroute
from router.user import router as Userroute

app = FastAPI()

app.include_router(Homeroute, prefix="/Home", tags=["Home Page"])
app.include_router(Userroute, prefix="/users", tags=["Authentication"])
app.include_router(Blogroute, prefix="/blog", tags=["Blog"])
app.include_router(Contactroute, prefix="/contact", tags=["Contacts"])
app.include_router(Aboutroute, prefix="/about", tags=["About"])



@app.get("/")
def loader():
    return {"message": "Welcome to THE Blog"}