class ClassA(object):
    def show(self):
        print("i am a method")

a=ClassA()
a.show()


# class Employee:
#     company = "Google"
#     def getSalary(self):
#         print("salary is 10k ")

# harry = Employee()
# harry.getSalary() # Employee.getSalary(harry)

# self is a parameter that can pass automatically
# if we dont pass self its trhow an error

class Employee:
    company = "Google"
    def getSalary(self):
        print(f"salary for this employee working in {self.company} is {self.salary} ")

harry = Employee()
harry.salary = 100000
harry.getSalary() # Employee.getSalary(harry)




