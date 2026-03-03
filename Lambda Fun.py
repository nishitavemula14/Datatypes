# Lambda Function
val = lambda i :i*2
print(val(25))

#Display the string using lambda function
str="Hello World!!"
(lambda str : print(str))(str)

#Multiply 3 Arguments
a = lambda i,j,k : i*j*k
print(a(10,92,8))

#Maximum of 2 numbers
res = lambda a,b : a if a>b else b
print(res(36,85))

#Square of a number
val = lambda k : k**2
print(val(2))

#Higher order functions (map())
l =[10,50,60,5,20]
def add(x):
    return x+5
nl = list(map(add, l))
print(nl)

#filter()
l =[5,-25,92,-10,0,-6]
nl = list(filter(lambda x:x<0,l))
print(nl)

#reduce()
from functools import reduce
a = [10,20,30,50]
sum = reduce(lambda x,y :x+y,a)
print(sum)

#Finding the maximum element
from functools import reduce
a = [10,60,852,900]
result = reduce(lambda x,y : x if x>y else y , a)
print(result)