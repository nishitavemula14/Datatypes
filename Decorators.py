#with @decor syntax
def decor(fun):
    def inner():
        print("GOOD MORNING BOSS!")
        fun()
        print("HAVE A NICE DAY!")
    return inner
@decor
def greet():
    print("HOW ARE YOU?")

greet()
#Without using @decorator
def decor(fun):
    def inner():
        print("GOOD MORNING")
        fun()
        print("HAVE A NICE DAY")
    return inner
def greet():
    print("Hru")
greet=decor(greet)
greet()
#Decorator with arguments
def decor(fun):
    def inner(name):
        print("WELCOME")
        fun(name)
        print("THANK YOU")
    return inner
def greet(name):
    print("HELLO",name)
greet = decor(greet)
greet("Nishitha")

#multiple decorators
def start(fun):
    def inner():
        print("START")
        fun()
        print("END")
    return inner
def decor(fun):
    def inner():
        print("WELCOME")
        fun()
        print("THANKYOU")
    return inner
@start
@decor
def greet():
    print("HOW R YOU")
greet()