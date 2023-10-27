from fastapi import APIRouter, HTTPException
from schemas.aboutschemas import About
from services.aboutservices import servicer

router = APIRouter()


# Endpoint to create an about article
@router.post("/write", status_code=201)
def write_about(about: About):
    servicer.about_service(about)
    return {"message": " About article saved!"}
    

# Endpiont to view or choose an about article
@router.get("/display/{about_id}", status_code=200)
def about_display(about_id: str):
    about = servicer.about_via_id(about_id)
    if about:
        return about
    else:
        raise HTTPException(status_code=404, detail="Sorry, could not load article an error occurred!!!")