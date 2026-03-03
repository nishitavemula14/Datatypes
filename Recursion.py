#Fibonacci
def fibonacci(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(6))


#Factorial
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(5))

#Reverse a string
def reverse_string(s):
    if len(s)==0:
        return s
    else:
        return s[-1]+reverse_string(s[:-1])
print(reverse_string("Hello World"))

#power of a X
def power(x,n):
    if n ==0:
        return 1
    else:
        return x*power(x,n-1)
print(power(2,3))
#sum of N natural numbers
def sum_n(n):
    if n==1:
        return 1
    else:
        return n+sum_n(n-1)
print(sum_n(5))