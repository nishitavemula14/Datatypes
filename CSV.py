import csv

with open("csv_demo.txt", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

#Writing a csv file
import csv

data = [
    ["Name","Age","City"],
    ["Nishitha",20,"Hyderabad"],
    ["Rahul",25,"Delhi"],
    ["Anu",21,"Chennai"]
]

with open("new.csv","w", newline = "") as file:
    writer = csv.writer(file)
    writer.writerow(data)

with open("new.csv","r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
#Reading csv ad dictionary
import csv

with open("csv_demo.txt","r") as file :
    reader = csv.DictReader(file)

    for row in reader:
        print(row["name"], row["subject"], row["marks"])

#Dict writer
import csv
data =[
    {"name":"Nishi","salary" : 50000},
    {"name":"Cherry","salary": 30000},
    {"name":"Disha","salary": 45000},
    {"name":"Bunny","salary": 49000},
    {"name":"Bittu","salary": 35000}
]
with open("students.csv","w", newline ="") as file:
    fieldnames = ["name", "salary"]
    
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(data)
print(data)

#Example
import csv
with open("students.txt","r") as file:
    reader = csv.reader(file) 

    for row in reader:
        print(row)
#WRITE DATA TO CSV FILE
import csv
data = [
    ["name","marks","category"],
    ["suresh",21,"fail"]
]
with open("students.txt","w", newline = "") as file:
    writer = csv.writer(file)
    writer.writerows(data)
#APPEND
import csv
new_row = ["Harika",62, "pass"]
with open("students.txt", "a", newline = "") as file:
    writer = csv.writer(file)
    writer.writerow(new_row)
#READ CSV FILE WITH DICTREADER
import csv
with open("students.txt", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["name"], row["marks"], row["category"])
#SEARCH DATA IN CSV
import csv

search_name= "Nishitha"

with open("students.txt","r") as file:
    reader=csv.DictReader(file)

    for row in reader:
        if row["name"] == search_name:
            print("marks:", row["marks"])