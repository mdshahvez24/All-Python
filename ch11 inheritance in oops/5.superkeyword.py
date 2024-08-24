# super -- super keyword is use to refer to the parent class it is specially use to when a class inherit from multiple parent classes and we want to call a method from one of the parent classes

class Parent:
    def p_method(self):
        print(" this is the method of parent class 1")

class Child(Parent):
    def c_method(self):
        print("this is the method of child class 2")
        super().p_method()

child_obj = Child()
child_obj.c_method()  #  his is the method of child class
# child_obj.p_method()  # this is parent method
child_obj.p_method()  # this is parent method 1

# super key -- use for  call constructor of super class

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        
       
class Programmer(Employee):

    # def __init__(self, name, id, lang):
    #     self.name=name
    #     self.id = id
    #     self.lang = lang

# use this insted of ↟

    def __init__(self, name, id, lang, dsg):
       super().__init__(name, id)
       self.lang = lang
       self.dsg = dsg

# rohan = Employee("Rohan das","420")
harry = Programmer("Harry","2345","python","Trainer")
print(harry.name)
print(harry.id)
print(harry.lang)
print(harry.dsg)












class Person:
    country = "India"

    def takeBreath(self):
        print("I am breathing 1...")

class Employee(Person):
    company = "Honda"

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreath(self):
        super().takeBreath()
        print("I am an Employee so I am luckily breathing 2..")

class Programmer(Employee):
    company = "Fiverr"

    def getSalary(self):
        print(f"No salary to programmer")

    def takeBreath(self):
        super().takeBreath()
        print("I am an Employee so I m luckiley breathing.+++.")

p = Person()
p.takeBreath()
# print(p.company) # throws an error bcz there is no company

e = Employee()
e.takeBreath()
# print(e.company)

pr = Programmer()
pr.takeBreath()