# A statement which are eexecuted by given condition is called conditional statement
# if condition:
# print("If condition is true then this statement will be executed")
# else:
# print("If condition is false then this statement will be executed")

# Here we can use below operators in conditional statement

# comparison operators - ==, !=, >, <, >=, <=
a = 15
b = 20
c = 15
if a == b:
    print("a and b are equal")
else:
    print("a and b are not equal")


if a > b:
    print("This is if statement")
elif a == c:
    print("This is elif statement")
elif a == b:
    print("This is elif2 statement")
else:
    print("This is else statement")

if a>b:
    if a==c:
        print("a and c are equal")
    else:
        print("else statement")
else:
    print("else2 statement") # print if first if condition is false