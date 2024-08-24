# with 2 parameter data transform outside from the class
class Mobile:

    @staticmethod     # decorator
    def show_model(m, p):
        model = m
        price = p
        print("Model:", model, "Price:", price)

realme = Mobile()
Mobile.show_model('Realme X', 1000)   # calling static Method

# passing membor of one class to another

class Student:
    # constructor
    def __init__(self, n, r):
        self.name = n
        self.roll = r

    # instance method 
    def disp(self):
        print("student name:", self.name)
        print("student roll:", self.roll)

class User:
    # static method
    @staticmethod
    def show(self):
        print("User Name:", self.name)
        print("User roll:", self.roll)
        # self.disp()

# creating object of student class

stu = Student("Harry", 101)
User.show(stu)



class Employee:
    company = "Google"

    def getSalary(self, signature):
        print(f"salary for this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod         # decorator
    def greet():          #static method
        print("Good Morning, Sir")

    @staticmethod
    def time():
        print("the time is 9 am")

harry = Employee()
harry.salary = 10000
harry.getSalary("thanks!")  # Employee.getSalary(harry)
harry.greet() # Employee.greet()
harry.time()
Employee.time() # the time is 9 am

