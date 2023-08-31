# A function is a block of code which execute when we call it.
# Types of function: Non-paramter function, parameter function, return type function

# Using "def" keyword we can define a function
# Function name should be in camel case - first letter should be small and second word first letter should be capital

# Non-parameter function
def nonParameterFunction():
    print("This is non-parameter function")

nonParameterFunction()

# Parameter function
def parameterFunction(name):
    print("This is parameter function")
    print("Name is", name)

parameterFunction("John")

# Return type function
def returnTypeFunction(a,b):
    c = a + b
    return c

d = returnTypeFunction(10, 5)
print(d)

# default value in function
def sumOFTwoNumber(a,b=5):
    c = a + b
    return c

d = sumOFTwoNumber(10)
print(d)

# Pass list in function
def listFunction(list):
    for x in list:
        print(x)

b = ["a", "b", "c"]
listFunction(b)

# Key and value as argument in function
def empData(name, age):
    print("Name is:", name)
    print("Age is:", age)

empData(name="John", age=25)

# Arbitrary arguments, *args - If we don't know how many arguments that will be passed into our function, add a ** before the parameter name in the function definition.
def empData2(**emp):
    print(emp)
empData2(name="John", age=25)

def methodThree():
    pass # we can pass this function