fruits = ["apple","banana","cherry"]
for index, value in enumerate(fruits):
    print(index,value)


fruits = ["apple","banana0","mango"]
for index, value in enumerate(fruits, start=1):
    print(index,value)

#example with strings
word ="Python"
for index , letter in enumerate(word):
    print(index,letter)

word = "Python"
for index , letter in enumerate (word , start=1):
    print(index,letter)

#example
numbers = [10,20,30,40]
for index ,value in enumerate(numbers):
    print("index:",index,"value:",value)

#example 2
numbers = [10,20,30,40]
for index , value in enumerate(numbers):
    if value ==20:
        print("position of 20 is:",index)

#print list of students wit their roll numbers
students=["Nishi","Vinnu","Shashi","Yash"]
for index, name in enumerate(students, start=1):
    print("Roll number:", index,"Name:",name)
#sum of list of numbers
numbers = [1,2,3,4,5]
total =0
for index, value in enumerate(numbers):
    total = total+value
print("sum of numbers is:",total)
#print even inde numbers
numbers =[10,20,30,20,60]
for index,value in enumerate(numbers):
    if index%2==0:
        print("even index:",index,"value:",value)