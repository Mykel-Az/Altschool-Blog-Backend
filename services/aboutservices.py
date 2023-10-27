from schemas.aboutschemas import About
import csv
from uuid import uuid1
from fastapi import HTTPException

class AboutService:
    def about_service(self, about: About):
        with open("Aboutdata.csv", "a", newline='') as data:
            writer = csv.writer(data)
            about_id=str(uuid1())
            writer.writerow([about_id, about.header, about.body])

    def about_via_id(self, id: str):
        with open("Aboutdata.csv", "r") as data:
            reader = csv.reader(data)
            for row in reader:
                if len(row)>=2 and row[0] == id:
                    return row
            raise HTTPException(status_code=404, detail="article not found")

servicer = AboutService()