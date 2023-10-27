from fastapi import APIRouter, HTTPException
from schemas.blogschemas import CreateBlog, Blog, Response
from services.blogservices import blogger
from services.userservice import authenticate
from router.user import login
from uuid import UUID
import csv

router = APIRouter()

# Endpoint to create a Blog
@router.post("/create", status_code=201)
async def write_blog(
    User_id: str,
    blog: CreateBlog
):
    if blogger.new_logger(User_id):
        details = blogger.get_details(User_id)
        user_id = details[0]
        first_name = details[2]
        last_name = details[3]
        myblog = blogger.create_blog(user_id, first_name, last_name, blog)
        return myblog
    else:
        raise HTTPException(status_code=403, detail="You are not logged in, log in to for Accessibility")
    

# Endpoint to view a Blog
@router.get("/view/{blog_id}", status_code=200)
async def view_blog(blog_id: str):
    myblog = blogger.blog_via_id(blog_id)
    return Response(data=myblog)


# Endpoint to edit a blog
@router.put("/edit/{blog_id}", status_code=201)
async def edit_blog(
    blog_id: str,
    user_id:str, 
    blog: CreateBlog
):
    if blogger.new_logger(user_id):
        if blogger.blogger_checker(user_id, blog_id):
            status = "edited"
            new_values = [blog.title, blog.blog_post, blog.time, status]
            blogger.update_blog(blog_id, new_values)
            return Response(message="Updated Successfully", data= new_values)
        else:
            raise HTTPException(status_code=403, detail="You cannot perform this action,i suggest try on a blog you created")
    else:
        raise HTTPException(status_code=403, detail="You are not logged in, log in to for Accessibility")


# Endpooint to delete a blog
@router.delete("/delete/{blog_id}", status_code=200)
async def delete_blog(
    blog_id: str,
    user_id:str
):
    if blogger.new_logger(user_id):
        if blogger.blogger_checker(user_id, blog_id):
            blogger.truncate_blog(blog_id)
            return Response(message="Blog deleted Successfully!!!")
        else:
            raise HTTPException(status_code=403, detail="You cannot perform this action,i suggest try on a blog you created")
    else:
        raise HTTPException(status_code=403, detail="You are not logged in, log in to for Accessibility")
