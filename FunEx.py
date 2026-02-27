#simple Calculator
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def division(a,b):
    if b==0:
        return "cannot divide by zero"
    else:
        return a/b
print(add(8,5))
print(sub(5,3))
print(multiply(5,2))
print(division(2,0))

#even number
def is_even(a):
    return a %2==0
num= 7
if is_even(num):
    print("its an even number")
else:
    print("its an odd number")


#Student Marks Calculator
def grade_calculator(marks):
    average=sum(marks)/ len(marks)

    if average >= 90:
      print("Grade A")
    elif average >= 75:
      print("Grade B")
    elif average >= 50:
        print("Grade C")
    else:
        print("Fail")
score =[65,85,75,90]
print("Grade",grade_calculator(score))

#vowels counting
def count_vowels(name):
    vowels ="aeiouAEIOU"
    count =0
    for char in name:
        if char in vowels:
            count+=1
    return count
print(count_vowels("Nicky"))



#Simple banking Statement
def deposit(balance,amount):
    return balance+amount
def withdraw(balance,amount):
    if amount>balance:
        print("Insufficient Funds")
        return balance
    else:
        return balance-amount
def check_balance(balance):
    print("current balance:",balance)

balance=1000
balance = deposit(balance,5000)
balance = withdraw(balance,2000)
check_balance(balance)