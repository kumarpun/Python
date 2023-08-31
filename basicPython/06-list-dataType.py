# Storing the different data types in order and list is changeable in run time. It allows duplicate values.
# Values should be assigned in square brackets "[]"

name_list1 = [1, "Python", 4.5, 5, 7]

# Access the values in a list using index
print(name_list1[1])

# Slicing - Getting substring from string [1:n-1]
print(name_list1[1:4])

# Get end values from list
a = name_list1[-1]
print(a)

# Get length of list
print(len(name_list1))

# Update the value in list
name_list1[1] = "Hello"
print(name_list1)

# Append the value in list
name_list1.append("World")
print(name_list1)

# Insert the value in list at specific index position - insert(index, value)
name_list1.insert(2, "World")
print(name_list1)

# Remove the value from list
name_list1.remove("Hello")
print(name_list1)

# Find the value in list
a = "World" in name_list1
print(a)

b = "World" not in name_list1
print(b)

# Iterate the list using for loop
for a in name_list1:
    print(a)

# Add two list  - Concatenation
name_list2 = [1, 2, 3]
name_list3 = [4, 5, 6]
name_list4 = name_list2 + name_list3
print(name_list4)

# Delete the list
del name_list1
print(name_list1)