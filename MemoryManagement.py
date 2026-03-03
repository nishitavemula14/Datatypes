#RefernceCounting
x = [10,20,30,40]
y=x
print(y)
print(id(x))
print(id(y))


#Garbage Collector
class A:
 def __init__(self):
    self.ref = None
a=A( )
b=A( )
a.ref = b         
b.ref = a

#VaribleScope (Local scope)
def demo():
    a = 100
    print(a)
demo()
#VaribleScope (Global scope)
a=500
def demo():
   print(a)
print(a)
demo()
print(a)

#Global keyword
a=52
def demo():
   global a 
   a=2
   print(a)
demo()
print(a)

#Garbage Collections
import gc
gc.collect()
print("Garbage collection executed")