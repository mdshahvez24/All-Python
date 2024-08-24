# class - class is a blue print of object

class DemoClass:
    a=10
    def sum(self):
        print(20+30)

object=DemoClass()
object1=DemoClass()
print(object.a)
print(object1.a)
object.sum()

class Employee:
    company = "Google"
    salary = 100

harry = Employee()
rajni = Employee()

# # Cretaing a instance atrribute salary for both the object
# harry.salary = 300
# rajni.salary = 400

harry.salary = 45

print(harry.salary)
print(rajni.salary) # it take atrribute salary from class



class Person:
    name = "Ali"
    occup = "Software devloper"
    networth = 10
    def info(self):
        print(f"{self.name} is a {self.occup}")

a = Person()
b = Person()
c = Person()

a.name = "subham"
a.occup = "Accuntant"

b.name = "leyakirsan"
b.occuo = "HR"

a.info()
b.info()
c.info()