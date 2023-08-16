# Storing the different data types in order and tuple is unchangeable in run time. It allows duplicate values.
# Values should be assigned in round brackets "()"

name_tuple1 = (1, "Python", 4.5, 5, 7)

# Access the values in a tuple using index
print(name_tuple1[1])

# Slicing - Getting substring from string [1:n-1]
print(name_tuple1[1:4])

# You can't update the value in tuple
# name_tuple1[1] = "Hello"
# print(name_tuple1)

# Get length of tuple
print(len(name_tuple1))
print(name_tuple1.count(5))

# You can't append the value in tuple
# name_tuple1.append("World")
# You can't insert the value in tuple at specific index position
# You can't remove the value from tuple

# Find the value in tuple
a = "Python" in name_tuple1
print(a)

# Iterate the tuple using for loop
for a in name_tuple1:
    print(a)

# Add two tuple  - Concatenation
name_tuple2 = (1, 2, 3)
name_tuple3 = (4, 5, 6)
name_tuple4 = name_tuple2 + name_tuple3
print(name_tuple4)

# Delete the tuple
del name_tuple1
