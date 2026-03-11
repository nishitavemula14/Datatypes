#Creating a class
class Student:
    def __init__(self , name , age):
        self.name = name
        self.age = age
    
    def display(self):
        print(self.name, self.age)
#Creating object
s1 = Student("Nishi",20)
s1.display()
#Example
class Car:
    def start(self):
        print("Car started")
C1 = Car()
C1.start()
#Multiple Objects
class Car:
    def __init__(self , brand):
        self.brand = brand
    
    def start(self):
        print(self.brand , "car started")
c1 = Car("BMW")
c2 = Car("THAR")

c1.start()
c2.start()
#Class with two methods 
class Calculator:
    def add(self, a, b):
        print("sum:",a + b)
    def multiply(self, a, b):
        print("product:",a * b)
c1 = Calculator()
c1.add(5,7)
c1.multiply(2,5)
#Bank Account
class BankAccount:

    def __init__(self,name,balance):
        self.name =  name
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print("Balance after deposit:",self.balance)
    
    def withdraw(self , amount):
        self.balance -= amount
        print("Balance after withdraw:",self.balance)

b1=BankAccount("Nishi",5000)
b1.deposit(500)
b1.withdraw(200)
#Rectangle Area
class Rectangle:
    def __init__(self, length, width):
       self.length = length
       self.width = width
    def area(self):
        print("Area:", self.length * self.width)

a1 = Rectangle(5,3)
a1.area()
#Book Class
class Book:
    def __init__(self , bookname , author):
        self.bookname = bookname
        self.author = author
    
    def display(self):
        print("The Title is:", self.bookname)
        print("The Author is:", self.author)
b2 = Book("Physics", "John")
b2.display()
#Circle Area
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        print("The area of circle is:", 3.14 * self.radius * self.radius)
c2 = Circle(4)
c2.area()