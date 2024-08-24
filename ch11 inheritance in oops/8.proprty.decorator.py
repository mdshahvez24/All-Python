class Employee:
    company = "Bharat gas"
    salary = 4500
    salarybonus = 500
    # totalSalary = 5000

    @property   #getter
    def totalSalary(self):
        return self.salary + self.salarybonus
    @totalSalary.setter
    def totalSalary(self, val):
        self.salarybonus = val -self.salary


e = Employee()
print(e.totalSalary)
e.totalSalary = 5800
print(e.salary)
print(e.salarybonus)

