#Create or dump a file
import json
data = {
    "name":"Nishi",
    "age": 20,
    "salary":50000
}

with open("data.json", "w") as file:
    json.dump(data , file)
#Load
import json
with open("data.json", "r") as file:
    data = json.load(file)

print(data)
print(type(data))
#Write JSON into file
import json
data =  {
    "name":"cherry",
    "age": 17,
    "grade":"A"
}

with open("students.json","w")as file:
    json.dump(data , file)
#Read JSON from file
import json
with open("students.json","r") as file:
    data = json.load(file)
print(data)
print(type(data))
#Example with list
import json
students = [
            
            {"name":"raja","marks":95,"Rank":1},
            {"name":"rahul","marks":82,"Rank":3},
            {"name":"shree","marks":75,"Rank":4},
            {"name":"pavani","marks":90,"Rank":2}
]
json_data = json.dumps(students, indent=4)
print(json_data)