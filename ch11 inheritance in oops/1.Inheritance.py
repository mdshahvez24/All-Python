class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id 
    
    def showDetails(self):
        print(f"the name of Employee is {self.name} and his id is {self.id} ")

# employee k saare method programmer k pass aagye 

class Programmer(Employee):
    def showlanguage(self):
        print("the default language is Python")

# emp = Employee("Ali", 120)
# emp.showDetails()

emp2 = Employee("harry",121)
emp2.showDetails()
emp2 = Programmer("harry",121)
emp2.showlanguage()




######## Ist program  ######################
class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id 
    
    def showDetails(self):
        print(f"the name of Employee is {self.name} and his id is {self.id} ")

# emp = Employee("Ali", 120)
# emp.showDetails()

emp2 = Employee("harry",121)
emp2.showDetails()
