# Create a class employee and add salary and increment properties to it write a method salary after increment method with property decoder with a setter which change the value of increment based on the salary.

class Employee:
    salary = 1000
    increment = 1.5

    @property
    def salaryAfterIncrement(self):
            return self.salary*self.increment

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, sai):
        self.increment = sai/self.salary

e = Employee()
print(e.salaryAfterIncrement)

print(e.increment)
e.salaryAfterIncrement = 2000 
print(e.increment)