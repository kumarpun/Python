"""
self represent instance of class - this method belongs to this class
"""


class EmployeeDetails:
    def __init__(self, name, number, address):
        self.name = name
        self.number = number
        self.address = address

    def empDetails(self):
        print("name :", self.name)
        print("number :", self.number)
        print("address :", self.address)

    def empName(self):
        print("Employee name is :", self.name)


emp = EmployeeDetails("kumar", 986517, "nepal")
emp.empDetails()
emp.empName()
