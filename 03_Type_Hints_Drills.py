# 1

# Normal
age=29
name="Abrar"
height=174.5
is_true=True


# Hinted
age:int=29
name:str="Abrar"
height:float=174.5
is_true:bool=True



# 2

# Normal
def greet(name):
    return f"Hello {name}"

# Hinted
def greet(name:str):            # name is string
    return f"Hello {name}"


# 3

#Normal
def square(number):
    return number*number

# Hinted
def square(number:int) -> int:
    return number*number


# 4 


# Normal
def add(a,b):
    return a+b

# Hinted
def add(a:int,b:int) -> int:
    return a+b


# 5

# Normal 
def average(a,b):
    return (a+b)/2

# Hinted
def average(a:int,b:int) ->float:
    return (a+b)/2


# 6

# Normal
numbers=[1,2,3,4,5,6]       # list


# Hinted
from typing import List
numbers:list[int]=[1,2,3,4,5,6]

# it contins integers

# 7 

# Normal
name=["Abrar","Ali","Ahmed"]


# Hinted
from typing import List
name:list[str]=["Abrar","Ali","Ahmed"]

# it contains strings



# 8

# Normal
person=("Abrar",30)     # Tuple


# Hinted

from typing import Tuple
person:tuple[str,int]=("Abrar",30)

# it contains string and integers


# 9

# Normal
score={"Abrar":90,"Ali":92}

# Hinted
from typing import Dict
score=dict[str,int]={"Abrar":90,"Ali":92}


# 10 (Union)

# Normal
student="Ab"
id=900
# After union
student_id="Ab900"

# Hinted
student_id:str|int="Ab900"      # str|int means strins and integers are allowed.

# student_id can be a string or an integer

# 11 variable

# Normal
name = "Abrar"
age = 29
height = 174.5
is_active = True

# Hinted
name:str = "Abrar"
age:int = 29
height:float = 174.5
is_active:bool = True


# 12 list

# Normal
numbers = [10, 20, 30, 40]
cities = ["Munich", "Berlin", "Hamburg"]

# Hinted
numbers:list[int] = [10, 20, 30, 40]
cities:list[str] = ["Munich", "Berlin", "Hamburg"]



# 13 Tuple

# Normal
student = ("Abrar", 29)

# Hinted
student:tuple[str,int] = ("Abrar", 29)



#  14 Dictionary

# Normal
marks = {   "Python": 85,
            "DSA":    70,
            "Math":   60  }

# Hinted
marks:tuple[str,int] = {   "Python": 85,
            "DSA":    70,
            "Math":   60  }



# 15 union

# Normal
student_id = "ID123"

# Hinted
student_id: str|int = "ID123"



# 16 functionwith return type

# Normal
def square(number):
    return number * number

# Hinted
def square(number:int) -> int:
    return number * number



# 17 function with Float Type

# Normal
def average(a:int, b:int) -> float:
    return (a + b) / 2



# 18 Function returning string

# Normal
def make_message(name, age):
    return f"{name} is {age} years old"

# Hinted
def make_message(name:str, age:int) ->str:
    return f"{name} is {age} years old"


# 19 List as function parameter

# Normal
def total(numbers):
    return sum(numbers)

# Hinted
def total(numbers:list[int]) -> int:
    return sum(numbers)



# 20 Dictionary as function Parameter

# Noarmal
def get_python_marks(marks):
    return marks["Python"]

# Hinted
def get_python_marks(marks:dict[str,int]) -> int:
    return marks["Python"]