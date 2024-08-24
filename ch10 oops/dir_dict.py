# dir function return a list of all the attributes and methods available for an object

x = [1,2,3]
print(dir(x))

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("jhon", 30)
print(p.__dict__)  #{'name': 'jhon', 'age': 30}