import csv

class Homer:
    def Home_checker(self):
        rows = []
        with open("Blogdata.csv", "r") as data:
            reader = csv.reader(data)
            next(reader)
            for row in reader:
                rows.append(row)
            return rows
        

all_blogs = Homer()