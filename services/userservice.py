from schemas.userschema import UserBase, User
from fastapi import HTTPException
from uuid import uuid1
import csv, re

class Authentication:
    def signup_service(self, user: UserBase):
        with open("Userdata.csv", "a", newline='') as data:
            writer = csv.writer(data)
            user_id=str(uuid1())
            with open("Userdata.csv", 'r') as data:
                reader = csv.reader(data)
                for row in reader:
                    if len(row)>=6 and row[1] == user.username :
                        raise HTTPException(status_code=400, detail="Username already exist, try another")
                    if not password_validation(user.password):
                        raise HTTPException(status_code=400, detail="password should be at least eight characters long and include a mix of upper and lowercase letters, numbers, and special symbols")
                else:
                    writer.writerow([user_id, user.username, user.first_name, user.last_name, user.email, user.password])
        

    def login_checker(self, username: str, password: str):
        with open("Userdata.csv", "r") as data:
            reader = csv.reader(data)
            next(reader)
            for row in reader:
                if len(row)>=6 and row[1] == username and row[5] == password:
                    return True
                                
            return False
    
    
    def logger(self, username, new_value):
        with open("Userdata.csv", "r") as data:
            reader = csv.reader(data)
            rows = list(reader)
        for row in rows:
            if len(row)>=6 and row[1] == username:
                row[6:7] = new_value

        with open("Userdata.csv", "w", newline="") as data:
            writer = csv.writer(data)
            for line in rows:
                writer.writerow(line)


    def user_via_id(self, id: str):
        with open("Userdata.csv", "r") as data:
            reader = csv.reader(data)
            for row in reader:
                if len(row)>=5 and row[0] == id:
                    return row
            raise HTTPException(status_code=404, detail="user not found")

authenticate = Authentication()

def password_validation(password):
    if len(password) < 8:  
        return False  
    if not re.search("[a-z]", password):  
        return False  
    if not re.search("[A-Z]", password):  
        return False  
    if not re.search("[0-9]", password):  
        return False  
    return True 
    


