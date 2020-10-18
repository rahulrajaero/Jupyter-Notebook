# Creating the employee class
class Employee():
    """
    This class stores the Name and Age of employee.
    """
    
    # class attribute
    grade = 1
    
    # constructor
    def __init__(self, name, age):
        # instance attributes
        self.name = name
        self.age = age
    
    # get name of employee
    def get_name(self):
        return self.name

    # get age of employee
    def get_age(self):
        return self.age

# create object of Employee class
employee1 = Employee("Bob", 23)
print("Employee 1 belongs to grade: ", employee1.__class__.grade)

print("Name of Employee 1: "+employee1.get_name())
print("Age of Employee 1:",employee1.get_age())