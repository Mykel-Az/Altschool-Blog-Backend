import csv
from uuid import UUID
from fastapi import HTTPException
from schemas.blogschemas import CreateBlog, Blog

   
class Blogger:
    def get_details(self, user_id:str):
        with open("Userdata.csv", "r") as data:
            reader = csv.reader(data)
            for row in reader:
                if len(row)>=6 and row[0] == user_id:
                    return row
            raise HTTPException(status_code=404, detail="User does not exist!!")


    def create_blog(self, user_id:str, first_namer:str, last_namer:str, blog: CreateBlog):
        rows = []
        with open("Blogdata.csv", "r") as data:
            reader = csv.reader(data)
            next(reader)
            for row in reader:
               rows.append(row)

        with open("Blogdata.csv", "a", newline="") as data:
            writer = csv.writer(data)
            blog_id=str(UUID(int=len(rows) + 1)) 
            time_stamp=str(blog.time)
            writer.writerow([blog_id, user_id, first_namer, last_namer, blog.title, blog.blog_post, time_stamp])
            myblog = ([blog_id, user_id, blog.dict(), first_namer, last_namer])
            return myblog
            

    def blog_via_id(self, id: str):
        with open("Blogdata.csv", "r") as data:
            reader = csv.reader(data)
            for row in reader:
                if len(row)>=5 and row[0] == id:
                    return row
            raise HTTPException(status_code=404, detail="Blog not found")

        

    def update_blog(self, blog_id:str, new_values):
        with open("Blogdata.csv", "r") as data:
            reader = csv.reader(data)
            rows = list(reader)
        for row in rows:
            if len(row)>=7 and row[0] == blog_id:
                row[4:8] = new_values

        with open("Blogdata.csv", "w", newline="") as data:
            writer = csv.writer(data)
            for line in rows:
                writer.writerow(line)

    def new_logger(self, user_id:str):
        with open("Userdata.csv", "r") as data:
            reader = csv.reader(data)
            rows = list(reader)
            status = "Logged In"
            for row in rows:
                if len(row)>=6 and row[0]== user_id and row[6] == status:
                    return True
            return False
        

    def blogger_checker(self, user_id:str, blog_id:str):
        with open("Blogdata.csv", "r") as data:
            reader = csv.reader(data)
            rows = list(reader)
            for row in rows:
                if len(row)>=7 and row[0] == blog_id and row[1] == user_id:
                    return True
            return False
       

    def truncate_blog(self, blog_id: str):
        rows = []
        with open("Blogdata.csv", "r") as data:
            reader = csv.reader(data)
            info = list(reader)
        for row in info:
            if len(row) >= 7 and row[0] != blog_id:
                rows.append(row)
            elif row == []:
                rows.append(row)

        with open("Blogdata.csv", "w", newline="") as data:
            writer = csv.writer(data)
            for line in rows:
                writer.writerow(line)


blogger = Blogger()



