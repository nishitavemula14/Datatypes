def numbers():
    yield 1
    yield 2
    yield 3

g = numbers()
print(next(g))
print(next(g))  
print(next(g))
#using loop
def numbers(a):
    for i in range(a):
        yield i
g = numbers(5)
for num in g:
    print(num)

#Fibonacci series using generator
def fibonacci(n):
    a,b=0,1
    for i in range(n):
        yield a
        a,b=b,a+b
for num in fibonacci(10):
    print(num)
#generator expression
g = (x**2 for x in range(5))
for i in g:
    print(i)

#Square of a number using generator expression
def square_numbers(n):
    for i in range(1, n+1):
        yield i*i

for num in square_numbers(5):
    print(num)
#Reverse a string using generator expression
def reverse_string(text):
    for char in text[::-1]:
        yield char
for char in reverse_string("Python"):
    print(char)
#Multiplication table
def table(n):
    for i in range(1,11):
        yield n*i
for num in table(5):
            print(num)
#odd numbers using generator expression
def odd_numbers(n):
    for i in range(n):
        if i%2 ==1:
            yield i
for num in odd_numbers(10):
    print(num)
#Cube of a number
def cube_numbers(n):
    for i in range(1,n+1):
        yield i**3
for num in cube_numbers(5):
    print(num)
#Countdown using generator expression
def count(n):
    while n>0:
        yield n
        n-=1
for num in count(5):
    print(num)
#postive numbers
def positive_numbers(a):
    for i in a:
        if i>0:
            yield i
n = [20,58,-36,-75]
for num in positive_numbers(n):
    print(num)
#coverting list into uppercase
def uppercase(words):
    for word in words:
        yield word.upper()
words =["hi","this","is","nicky"]

for w in uppercase(words):
    print(w)
#Genarator for characters in a string
def string_characters(text):
    for ch in text:
        yield ch
for c in string_characters("Python"):
      print(c)
#Generator Expression
g =(x for x in range(10) if x%2==0)
for num in g:
    print(num)
#using next() with generator expression
a = (x**2 for x in range(5))
print(next(a))
print(next(a))      
print(next(a))
print(next(a))
print(next(a))
#sum of numbers
g =(x for x in range(1,10))
print(sum(g))
#Coverting stings into uppercase using generator expression
words=["pugee","is","good","at","listening"]
g=(word.upper() for word in words)
for w in g:
    print(w)
#Filtering positive numbers
numbers = [10,-95,-10,35,20]
g =( x for x in numbers if x >0)
for num in g:
    print(num)