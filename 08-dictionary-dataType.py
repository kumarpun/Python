# Dictionaries are the key and value pairs written in curly brackets "{}"

# Create the dictionary
employeeData = {
    "name": "John", 
    "age": 29
    }

print(type(employeeData))
print(employeeData)

# Access the value from dictionary using key
print(employeeData["name"])

# Update the value in dictionary
employeeData["name"] = "Peter"
print(employeeData)

# Add the key and value in dictionary
employeeData["salary"] = 100000
print(employeeData)

# length of dictionary
print(len(employeeData))

# Copy the dictionary to another dictionary
employeeData1 = employeeData.copy()
print(employeeData1)

# Iterate the value using for loop
for a in employeeData.keys():
    print(employeeData[a])

# Iterate both key and value using for loop
for a, b in employeeData.items():
    print(a, b)

# Remove the value from dictionary
employeeData.pop("name")
print(employeeData)

# Clear the dictionary
employeeData.clear()
print(employeeData)

# Delete the dictionary
del employeeData