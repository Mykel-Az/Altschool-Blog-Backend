from fastapi import APIRouter, HTTPException
from schemas.contactschema import Contact, Response
from services.contactservice import reachout


router = APIRouter()

#Endpoint to create a contact
@router.post("/create", status_code=201)
async def create_contact(person: Contact):
    reachout.contact_service(person)
    return Response(message="Thank You, we will get back to you as soon as possible")


#Endpoint to check all contacts
@router.get("/List", status_code=200)
async def contacts_list():
    contacts = reachout.contact_checker()
    if contacts:
        return Response(message="List of contacts", data=contacts)
    else:
        raise HTTPException(status_code=400, detail="Something went wrong!!!")


#Endpoint to get a particular contact
@router.get("/contact/{id}", status_code=200)
async def get_by_id(id:str):
    contact = reachout.contact_via_id(id)
    return Response(message="contact requested", data=contact)

