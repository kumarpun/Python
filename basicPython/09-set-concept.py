# Storing the different data type values in order and set is changeable in run time. It doesn't allow duplicate values.
# Values should be assigned in curly brackets "{}"
# Example: name_set = {1, "Python", 4.5, 5, 7}

# Create the set
name_set = {1, "Python", 4.5, 5, 1}
print(name_set) # 1 get printed only once
print(type(name_set))

# We can't insert the value in set once it is created, but we can add the value in set
name_set.add("Hello")
print(name_set)

# length of set
print(len(name_set))

# Remove the value from set
name_set.remove("Hello")
print(name_set)

# Discard the value from set - it will not throw error if value is not present in set
name_set.discard("Hello")
print(name_set)

# pop the value from set - it will remove the value from set
name_set.pop()
print(name_set)

# Join two sets - Union
name_set1 = {1, 2, 3}
name_set2 = {1, 5, 6}
name_set3 = name_set1.union(name_set2)
print(name_set3)

# Iterate the set using membership operator
for a in name_set3:
    print(a)

# Find the value in set using membership operator
a = "Python" in name_set3
print(a)

# clear the set
name_set3.clear()
print(name_set3)

# Delete the set
del name_set3