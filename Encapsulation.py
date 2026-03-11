#Public Variable
class Student:
    def __init__(self,name):
        self.name=name  #public variable
s = Student("Nishi")
print(s.name)

#Protected Variables
class Student:
    def __init__(self,name):
        self._name=name  #protected variable
s = Student("Raji")

print(s._name)

#Private Variables
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  #private variable
    def show_balance(self):
        print("balance is :",self.__balance)

b = BankAccount(5000)

b.show_balance()
#Enapsulation with setter and getter
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance
    
    def set_balance(self,amount):
        self.__balance = amount

v = BankAccount(10000)
print(v.get_balance())
v.set_balance(500)

print(v.get_balance())

#Password checker
class Mobile:
    def __init__(self):
        self.__password = "1234"
    def unlock(self,pwd):
        if pwd == self.__password:
            print("phone unlocked")
        else:
            print("wrong password")

m = Mobile()
m.unlock("2586")

#Student Marks
class Student:
    def __init__(self,marks):
        self.__marks = marks   #private variable
    def get_marks(self):
        return self.__marks
    def set_marks(self, m):
        self.__marks = m

y = Student(85)

print("marks:", y.get_marks())

y.set_marks(90)

print("Updated Marks:", y.get_marks())

#Employee Salary
class Employee:

    def __init__(self, salary):
        self.__salary = salary
    def get_salary(self):
        print("Salary:", self.__salary)
    def increase_salary(self,amount):
        self.__salary += amount

e = Employee(30000)

e.get_salary()

e.increase_salary(3000)

e.get_salary()
#Car Speed control
class Car:
    def __init__(self):
        self.__speed = 0
    def accelerate(self):
        self.__speed += 10
        print("Speed:", self.__speed)
    def brake(self):
        self.__speed -= 5
        print("Speed:", self.__speed)

h = Car()

h.accelerate()
h.accelerate()
h.brake()

#ATM pin
class ATM:
    def __init__(self):
        self.__pin = 2856
    def check_pin(self, entered_pin):
         if entered_pin == self.__pin:
             print("Access Granted")
         
         else:
             print("wrong pin")
a = ATM()
a.check_pin(1234)
a.check_pin(2856)

#Abstract class
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Square(Shape):

    def __init__(self , side):
        self.side = side
    def area(self):
        print("Area:", self.side * self.side)

x = Square(4)
x.area()

#Polymorphism
class Dog:
    def sound(self):
        print("dog barks")
class Cat:
    def sound(self):
        print("cat meows")
d= Dog()
c=Cat()
d.sound()
c.sound()
#Polymorphism with operator
print(5 + 10)
print("Hello" + "World")
#Polymorphism using Inheritance (Method Overriding)
class Animal:
    def sound(self):
        print("Animal makes sound")
class Dog(Animal):
    def sound(self):
        print("Dog barks")
class Cat(Animal):
    def sound(self):
        print("cat meows")

p=Dog()
j=Cat()
p.sound()
j.sound()