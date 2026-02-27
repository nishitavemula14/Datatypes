#defining function
def greet():
    print("Hello")
    print("Good Morning")
greet()

#function with Parameters
def add(x,y):
    a=x+y
    print(a)
add(5,7)

#Function with Arguments with return Value
def add(x,y):
    return x+y
result=add(2,3)
print(result)

#function with default parameter
def add(a=5,b=7):
    c=a+b
    print(c)
add(a=15,b=10)
add(b=30)  
    
#keyword Arguments
def intro(name,age):
    print("Name",name)
    print("age",age)
intro("John",25)

def intro(name,age):
    print("Name",name, "Age",age)
intro("John",25)