#Parent class
class Employee:
    company = "Google"

    def showDetails(self):
        print("this is an Employee")

#child class or derived class
class Programmer(Employee):
    language = "Python"
    # company = "Youtube"

    def getLanguage(self):
        print(f"this language is {self.language}")

    def showDetails(self): # overriding
        print("this is an programmer")

e = Employee()
p = Programmer()
e.showDetails()
p.showDetails()  
print(p.company)



