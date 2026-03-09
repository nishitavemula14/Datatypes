#zip()
names = ["ram","sam","geetha"]
marks = [85,92,36]
for name,mark in zip(names,marks):
    print(name,mark)
#enumerate
fruits =["apple","banana","orange","mango"]
for index, fruit in enumerate(fruits):
    print(index,fruit)
#List Comprehension
numbers = [1,2,3,4,5]
squares = [x*x for x in numbers]
print(squares)
#loop with condition 
numbers=[1,2,3,4,5,6]
even = [x for x in numbers if x%2==0]
print(even)
#Looping through Dictionary
student = {"name": "ricky", "age":"25","marks":"65"}
for key, value in student.items():
    print(key,value)
#break/else 
numbers = [1,6,3,7]
for num in numbers:
    if num %2==0:
        print("Even number found")
        break
    else:
        print("even number not found")
#Efficient iteration
numbers = [1,2,3,4]
for num in numbers:
    print(num)
#Iteration
numbers=[1,2,3,4]
for i in range(len(numbers)):
    print(numbers[i])
#List comprehension
squares = [x*x for x in range(5)]
print(squares)
#even number 
even = [x for x in range (10) if x%2==0]
print(even)
#String conversion
names=["ram","sita","lucky"]
upper = [name.upper() for name in names]
print(upper)
#using if-else
nums=[1,5,3,2]
result = ["even" if x%2==0 else "odd" for x in nums]
print(result)