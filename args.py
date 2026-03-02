def add_num(*args):
    total = 0
    for num in args:
        total+=num
    return total
print(add_num(10,66,85,36))
print(add_num(325,85,963))


#greet with multiple names
def greet(greeting,*names):
    for name in names:
        print(f"{greeting},{name}")
greet("Hello","Choco","Lucky","Nicky")

#unpacking

def add(*args):
   return sum(args)

numbers=[1,2,3,4]
print(add(*numbers))
#unpacking
elements=[1,2,3,4]
print(elements)
print(*elements)

#example
def order_pizza(size, *toppings):
    print(f"order a {size} pizza with the following toppings:")
    for topping in toppings:
        print(f"-{toppings}")

order_pizza("large","pepperoni","olives")
      

#**kwargs
def order_pizza(size, *toppings,**details):
    print(f"order a {size} pizza with the following toppings:")
    for topping in toppings:
        print(f"-{toppings}")
    print("\nDetails of the order are:")
    for key,value in details.items():
        print(f"- {key}:{value}")

order_pizza("large","pepperoni","olives", deliver = True, tip=5)
      