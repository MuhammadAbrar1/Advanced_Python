# Example a function
def add(a,b):
    return a+b
# Q. is "a" an integer?, a float?, a string?, a list?


def add(a: int, b: int):    # Type Hints allows the reader to know
    return a+b

# Type Hints can be considered as "Notes for readers"

"""important to note"""
# type Hint does not force python i.e.

a:int="Abrar"  # it wil still work.



# Variable Type Hints

age=29              # Normal variable
age:int=29          # type hinted   (it is read as "age should be an integer)


name="Abrar"        # Normal Variable
name:str="Abrar"    # type hinted   (it is read as "name should be a string")



# Function Parameters Hints

def greet(name):        # Normal function
    print(name)

def greet(name:str):    # Type Hinted   (it is read as "name should be a string")
    print(name)



# Return type Hints

def square(n):                  # normal function(not Hinted)
    return n*n

def square(n: int) -> int:      # the arrow means that This function returns as an integer
    return n*n



# Lists

number=[1,2,3]                  # normal

from typing import list
number: list[int]=[1,2,3]       # Hinted --> # it is read as "A list containing Integers" means list of integers



# Tuple

name_age=("Abrar",30)                       # normal

from typing import Tuple
name_age: Tuple[str,int]=("Abrar",30)       # Hinted

#  it is read as "Tuple containing string, Integer"



# Dictionaries

score={"Abrar":"84"}                        # Normal 

from typing import Dict
score:dict[str,int]={"Abrar":90,"Ali":90}   # Hinted

# it is read as "Dictionary whose keys are strings and values are integers"