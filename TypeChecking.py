def add(a: int , b: int) -> int:
    return a + b
results = add(5,3)
print(results)

#type hint for variables
name: str = "Nishitha"
age: int = 20
marks: float = 92.5
is_student: bool = True
print(name, age , marks, is_student)
#List
from typing import List
numbers: List[int] = [1,2,3,4]
print(numbers)
#Multiple types(Union)
from typing import Union
def square(num: Union[int,float])->float:
    return num*num

print(square(5))
print(square(2.5))
#Arguments
from typing import Callable

def operate(func: Callable[[int,int],int], a:int , b:int) -> int:
    return func(a,b)

def add(x:int,y:int) -> int:
    return x+y

print(operate(add , 4 , 5))
#example
def add(a: int, b: int) -> int:
    return a + b

print(add.__annotations__)