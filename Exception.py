try:
    x=10/2
except ZeroDivisionError:
    print("Error")
else:
    print("Successful:",x)
finally:
    print("Always runs.")



#File reading example
try:
    file=open("data.txt","r")
    content=file.read()
except FileNotFoundError :
    print("File not found")
else:
    print("file content",content)
finally:
    print("closing program")

#User-defined exceptions
class voting(Exception):
    pass
try:
    age=17
    if age<18:
        raise voting("your not eligible for voting")
    print("your not eligible")
except voting as v:
    print("Voting Error:",v)
except ValueError:
    print("invalid input")
#other example
class voting(Exception):
    def __init__(self,age):
        self.age=age
        super().__init__(f"age {age} is below 18. Not eligible for voting")
def check_voting_eligibility(age):
    if age < 18:
         raise voting(age)
    return"eligible to vote"
try:
    age=21
    message = check_voting_eligibility(age)
    print(message)
except voting as v:
    print("voting Error:",v)
except ValueError:
    print("please enter a valid age")
