""" the walrus operator allows to assign values to variables as part of an expression"""

# Examples

# 1
my_list=[1,2,3,4]
if (n:=len(my_list))>3:
    print(n)
print()


# 1.1
new_list=[3,6,1]
if (m:=len(new_list))<5:
    print(f"list is too short.{m} elements, expected=>5")
print()


# 2
if (name:="Muhammad Abrar"):
    print(name)
print()


# 3
(x:=10+5)
print(x)
print()


# 4
text="python"
if (length:=len(text))>5:
    print(length)
print()


# 5
student={"name":"Abrar"}
if (value:=student.get("name")):
    print(value)

# 6
count=5
while (n:=count)>0:
    print(n)
    count-=1
print()


# 7
print((x:=10)+20)
print()


# 8

number=len([1,2,3])
if number>2:
    print(number)

"""convert  to walrus style"""

l=[1,2,3]
if (number:=len(l))>2:
    print(number)
print()


# 9
name =input("Name: ")
if name:
    print(f"Hello {name}")

"""convert this to walrus style"""
if (new_name:=input("Name: ")):
    print(f"Hello {new_name}")
print()


# 10
result=50*2
print(result)

"""convert this to walrus style"""

print(rslt:=50*2)


