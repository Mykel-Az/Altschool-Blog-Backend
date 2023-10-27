import csv

def user_csv():
    header = ["User_Id", "Username", "First_name", "Last_name", "Email", "Password", "Logger"]

    with open("Userdata.csv", "w") as data:
        writer = csv.writer(data)
        writer.writerow(header)

user_csv()

def blog_csv():
    header = ["Blog_Id", "User_Id", "First_name", "Last_name", "Blog_title", "Blog_post", "Time_posted", "Time_Edited"]

    with open("Blogdata.csv", "w") as data:
        writer = csv.writer(data)
        writer.writerow(header)

blog_csv()

def contact_csv():
    header = ["id", "Name", "Email", "Subject", "Message"]

    with open("contactdata.csv", "w") as data:
        writer = csv.writer(data)
        writer.writerow(header)

contact_csv()

def about_csv():
    header = ["id", "Header", "Body"]

    with open("Aboutdata.csv", "w") as data:
        writer = csv.writer(data)
        writer.writerow(header)

about_csv()