# it is publically accessible from out side by default
# Public

class Emp:
    def __init__(self):
        self.name = "harry"

e = Emp()
print(e.name)  # harry

# it can be acccess indirectly
# private 

class Emp:
    def __init__(self):
        self.__name = "harry"

e = Emp()
# print(e.__name)  
print(e._Emp__name)  


# Protected access modufier

class Stud:
    def __init__(self):
        self._name = "harry"
    
    def _funName(self):  #protected method
        return "CodewithHarry"

class Subject(Stud):   #inherit class 
    pass

obj = Stud()
obj1 = Subject()

#calling by object of Student class

print(obj._name)
print(obj._funName())
# calling by object of subject class
print(obj1._name)
print(obj1._funName())