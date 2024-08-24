class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

e1=Employee("harry", 12000)
print(e1.name)   # harry
print(e1.salary)   # 12000

string = "jhon-12000"
e2 = Employee(string.split("-")[0],string.split("-")[1])
print(e2.name)
print(e2.salary)


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

#class mthd as alternative constructor

    @classmethod
    def fromStr(cls, string):
       return cls(string.split("-")[0],string.split("-")[1])

e1=Employee("harry", 12000)
print(e1.name)   # harry
print(e1.salary)   # 12000

string = "jhon-12000"
e2 = Employee.fromStr(string)
print(e2.name)
print(e2.salary)


class Person:
    def __init__(self, name, age):
        self.name= name
        self.age = age

    @classmethod
    def from_string(cls, string):
        name, age = string.split(',')
        return cls(name, int(age))

person = Person.from_string("jhon Deo, 30")
print(person.name, person.age)