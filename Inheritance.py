#Inheritance
class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")
d = Dog()
d.sound()
d.bark()
#Single Inheritance
class A:
    def display(self):
        print("ClassA")
class B(A):
    pass
obj = B()
obj.display()
#Multiple Inheritance
class A:
    def display(self):
        print("ClassA")
class B:
    def Show(self):
        print("classB")
class C(A,B):
    pass

obje = C()
obje.display()
obje.Show()
#Multilevel Inheritance
class A:
    def showA(self):
        print("ClassA")
class B(A):
    def showB(self):
        print("classB")
class C(B):
    def showC(self):
        print("classC")
name = C()
name.showA()
name.showB()
name.showC()

#Hierarchical Inheritance
class Parent:
    def show(self):
        print("Parent")
class Child1(Parent):
    pass
class Child2(Parent):
    pass
c1 = Child1()
c2 = Child2()

c1.show()
c2.show()
#Example(Single Inheritance)
class Animal:
    def eat(self):
        print("Animal eats food")
class Dog(Animal):
    def bark(self):
        print("Dog barks")
d = Dog()
d.eat()
d.bark()
#Multiple inheritance
class Father:
    def skills_father(self):
        print("Father: Driving")
class Mother:
    def skills_mother(self):
        print("Mother: Cooking")
class Child(Father,Mother):
    def skills_child(self):
        print("child: coding")
c = Child()
c.skills_father()
c.skills_mother()
c.skills_child()
#Multilevel inheritance
class Grandparents:
    def house(self):
        print("Grandfather owns a house")
class Parents(Grandparents):
    def car(self):
        print("Father owns a car")
class Child(Parents):
    def bike(self):
        print("child owns a bike")
s = Child()

s.house()
s.car()
s.bike()
#Hierarchical Inheritance
class Parent:
    def property(self):
        print("parents owns a property")
class Child1(Parent):
    def business(self):
        print("Child1 runs a business")
class Child2(Parent):
    def job(self):
        print("child2 does a job")
g1=Child1()
g2=Child2()

g1.property()
g1.business()

g2.property()
g2.job()