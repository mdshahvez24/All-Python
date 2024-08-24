class Employee:
    company = "Google"

    def __init__(self, name, salary, subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Employee is created!")

    def getDetails(self):
        print(f"the name of the employee is {self.name}")
        print(f"the salary of the employee is {self.salary}")
        print(f"the subunit of the employee is {self.subunit}")

    def getSalary(self, signature):
        print(f"salary for this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod
    def greet():
        print("good morning, sir")

    @staticmethod
    def time():
        print("the time is 9 am in the morning")

harry = Employee("harry", 100, "youtube")
# harry = Employee() --> This throws an error (missing 3 required positional arguments:)
harry.getDetails()