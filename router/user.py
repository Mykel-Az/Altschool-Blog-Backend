from fastapi import APIRouter, Form, HTTPException
from schemas.userschema import UserBase, Response
from services.userservice import authenticate
from typing import Annotated

router = APIRouter()
# Endpoint to create a user
@router.post("/signup", status_code=201)
async def signup(user: UserBase):
    authenticate.signup_service(user)
    return Response(message = f"Signup successfull, Welcome {user.first_name} You can now login as {user.username}")


# Endpoint for the user to signin
@router.post("/login", status_code=200)
async def login(
    username: Annotated[str, Form()],
    password: Annotated[str, Form()],
):
    user = authenticate.login_checker(username, password)
    if user:
        status = "Logged In"
        new_value = [status]
        authenticate.logger(username, new_value)
        return Response(message = f"Login successfull {username}", data= username)
    else:
        raise HTTPException(status_code=400, detail="Invalid Username or Password!!!")
    

# Endpoint for the user to view detials
@router.get("/userprofile/{user_id}")
async def userprofile(user_id: str):
    profile = authenticate.user_via_id(user_id)
    return Response(message="Your profile", data=profile)


# Endpoint to Signout
@router.post("/logout", status_code=200)
async def logout(
    username: Annotated[str, Form()],
    password: Annotated[str, Form()],
):
    user = authenticate.login_checker(username, password)
    if user:
        status = "Logged out"
        new_value = [status]
        authenticate.logger(username, new_value)
        return Response(message = f"Log Out successfull {username}")
    else:
        raise HTTPException(status_code=400, detail="Invalid Username or Password!!!")