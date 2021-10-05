import math
from array import array

print("hello");

print('mosh hamedani is my best youtube instructor')
name = "Muwonge lawrence the programmer"
age = 20
print('*' * 10)
print(f'my name is {name} and my age is {age} so you are welcome to python programming.')
print('*' * 10)
print("3 squared is " + str(3 ** 2))
print("-" * 50)
print("lets draw a right angled triangle")
for i in range(8):
    print("*" * i)

print('lets implement a sqaure')
for j in range(4):
    print("*" * 4)

print('lets implement a heart')
for j in range(1, 6):
    if j == 2:
        continue
    elif j == 3:
        print("-" * j)
        # break
    else:
        print("*" * j)
else:
    print("attempted all the times.")

message = """
hi muwonge 
this is lawrence the fullstack developer
how are you doing these days.
"""
course = "python Programming"
newString = course[:]
full = f"{message} \n l am learning {newString}"
print(full)
# print(newString)
print("The length of the above string is " + str(len(message)))
# ceil of the  values .
print(math.ceil(2.2))

x = input("x:")
y = int(x) + 9
print(f"x: {x} , y:{y}")

# working with comparison  operators
age = 22
message = "Eligible" if age >= 18 else "Not Eligible"
print(message)
print(type(5))

# infinite loops

while True:
    command = input(">:")
    print("Echo", command)
    if command.lower() == "quit":
        break

# using the zip function
list1 = [1, 2, 3]
list2 = [10, 20, 30]
print(list(zip(list1, list2)))

# swapping variables in python
x = 10
y = 11

x, y = y, x
print("x:", x)
print("y:", y)

# use of Arrays in python

numbers = array("i", [1, 2, 3])
print("This is from an array", numbers)
