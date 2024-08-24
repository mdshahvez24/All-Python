class Employee:
    company = "camel"
    salary = 100
    location = "Delhi"

# dender class
    # def changeSalary(self, sal):
    #     self.__class__.salary = sal

    @classmethod
    def changeSalary(cls, sal):
        cls.salary = sal

e = Employee() 
print(e.salary)
e.changeSalary(455)  #  instance attribute
print(Employee.salary)



class Emp:
    company = "AWS"
    def show(self):
        print(f"the name is {self.name} and company is {self.company}")

# class method decorator take a first argument as a class chnge the class attribute

    @classmethod
    def changeCompany(cls, newCompany):
        cls.company = newCompany

emp1 = Emp()
emp1.name = "harry"
# Emp.company = "Google"
emp1.changeCompany("tesla") # tesla
emp1.show()
print(Emp.company)