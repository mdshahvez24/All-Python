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
Employee.time()