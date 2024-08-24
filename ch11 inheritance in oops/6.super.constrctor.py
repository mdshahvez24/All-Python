class Person:
    country = "India"

    def __init__(self):
        print("Initializing Person..\n")

    def takeBreath(self):
        print("I am breathing 1...")

class Employee(Person):
    company = "Honda"

    def __init__(self):
        super().__init__()
        print("Initializing Employee..\n")

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreath(self):
        super().takeBreath()
        print("I am an Employee so I am luckily breathing 2..")

class Programmer(Employee):
    company = "Fiverr"

    def __init__(self):
        super().__init__()
        print("Initializing Programmer..\n")

    def getSalary(self):
        print(f"No salary to programmer")

    def takeBreath(self):
        super().takeBreath()
        print("I am an Employee so I m luckiley breathing.+++.")

# p = Person()
# p.takeBreath()
# print(p.company) # throws an error bcz there is no company

# e = Employee()
# e.takeBreath()
# print(e.company)

pr = Programmer()
# pr.takeBreath()