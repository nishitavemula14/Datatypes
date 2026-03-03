def add(a,b):
    result = a + b
    print(result)
add(2,3)
add(5,9)

#example1
def greet(name):
    return f"Hello {name}"
say_hello = greet
print(say_hello("Nicky"))

#PureFunctions
def add(n1,n2):
    return n1+n2
print(add(2,5))
print(add(2,5))

#Check even or odd (pure function)
def is_even(a):
    return a % 2 == 0 
print(is_even(5))
print(is_even(6))

#Factorial (pure function)
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))
print(factorial(5))

#Filter even numbers from a list
def get_even_numbers(a):
    return [ x  for x in a if x %2==0]
print(get_even_numbers([12,56,7,11,98,9,51]))

#Calculate the area of a circle
def area_of_circle(radius):
    pi =3.14159
    return pi*radius*radius
print(area_of_circle(5))


#Impure function
counter = 0
def increment():
    global counter
    counter += 1
    return counter
print(increment())
print(increment())

#Modifying a List
def add_items(lst):
    lst.append(100)
    return lst
numbers =[98,56,85,36]
add_items(numbers)
print(numbers)

#Print to console
def greet(name):
    print("Helllo",name)

greet("Nicky")

#Using random variables
import random
def roll_dice():
    return random.randint(1,6)

print(roll_dice())
print(roll_dice())