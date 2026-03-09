name = "Nishitha"
age = 20
print(f"My name is {name} and I am {age} years old")
#Using expressions
a=10
b=20
print(f"sum={a+b}")
#formatting numbers
price=25.6563
print(f"price= {price:.2f}")
#using pythonic loops
for i in range(3):
    print(f"number is {i}")
#Accessing a dictionary value
student = {"name":"Ram","marks":90}
print(f"{student['name']} scored {student['marks']}marks")
#Calling functions inside fstrings
def square(x):
    return x*x
print(f"Square of 4 is {square(4)}")