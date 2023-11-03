"""
Access all the method present in one class to other variable, properties
"""
from oops.Class import EmployeeDetails

class EmpDetails(EmployeeDetails):
    def empName2(self):
        self.empName()


emp = EmpDetails("Kp", 8765, "Nepal")
emp.empName2()
