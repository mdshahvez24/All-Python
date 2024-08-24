
class Employee:
    def __init__(self, name):
        self.name = name
        self.raise_amt = 0.02
    def showDetails(self):
        print(f"the name of the employee is {self.name} and amt is {self.raise_amt}")

# Employee.showDetails(emp1) #Harry

emp1 = Employee("Harry")
#we can change the instance variable  
emp1.raise_amt = 0.5 # harry amt is 0.5
emp1.showDetails() # Harry 0.02
emp2 = Employee("Rohan")
emp2.showDetails() # rohan 0.02


class Employee:
    companyName = "apple" # it is associated with class
    def __init__(self, name):
        self.name = name
        self.raise_amt = 0.02
    def showDetails(self):
        print(f"the name of the employee is {self.name} and raise amt in  {self.companyName} is {self.raise_amt}")

# Employee.showDetails(emp1) #Harry

emp1 = Employee("Harry")
emp1.raise_amt = 0.5 # harry amt is 0.5
emp1.companyName = "AWS"
emp1.showDetails() # Harry 0.02

emp2 = Employee("Rohan")
Employee.companyName = "Google"
print(Employee.companyName)
emp2.showDetails() # rohan 0.02
