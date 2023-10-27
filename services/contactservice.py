import csv
from fastapi import HTTPException
from schemas.contactschema import Contact
from uuid import uuid4


class ReachOut:
    def contact_service(self, person: Contact):
        with open("contactdata.csv", "a", newline='') as data:
            writer = csv.writer(data)
            Contact_id=str(uuid4())
            writer.writerow([Contact_id, person.name, person.email, person.subject, person.message])


    def contact_checker(self):
        rows = []
        with open("contactdata.csv", "r") as data:
            reader = csv.reader(data)
            next(reader)
            for row in reader:
                rows.append(row)
            return rows
            
    def contact_via_id(self, id: str):
        with open("contactdata.csv", "r") as data:
            reader = csv.reader(data)
            for row in reader:
                if len(row)>=4 and row[0] == id:
                    return row
            raise HTTPException(status_code=404, detail="contact not found")
        
reachout = ReachOut()