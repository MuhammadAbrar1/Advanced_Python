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