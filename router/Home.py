from fastapi import APIRouter, HTTPException
from services.homeservice import all_blogs
from schemas.contactschema import Response


router = APIRouter()

# Endpoint of Homepage where all blogs are displayed
@router.get("/BlogList", status_code=200)
async def blog_list():
    blogs = all_blogs.Home_checker()
    if blogs:
        return Response(message="List of Blogs", data=blogs)
    else:
        raise HTTPException(status_code=400, detail="Something went wrong!!!")