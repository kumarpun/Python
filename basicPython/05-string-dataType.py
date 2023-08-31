# Assigning single line string to a variable
name_1 = "Hello world"
# Assigning multi line string to a variable
name_2 = """This is a multi line string
            python tutorial
            in which we are learning
            about string data type
"""

print(name_1)
print(name_2)

# Slicing - Getting substring from string [1:n-1]
name_3 = name_1[1:3]
print(name_3)
name_4 = name_1[1:]
print(name_4)

# String length
print(len(name_1))

# Convert string to upper case
print(name_1.upper())

# Convert string to lower case
print(name_1.lower())

# Replace string with another string
print(name_1.replace("world", "python"))

# String concatenation - Joining two strings
a = "Hello"
b = "World"
c = a + " " + b
print(c)

# If string is present in sentence then it will return true otherwise false
# Membership operator - in, not in
d = "multi" in name_2
print(d)

e = "multi" not in name_2
print(e)