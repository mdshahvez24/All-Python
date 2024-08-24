class Student:
    __name="Ravi" # private variable
    def __init__(self):
        print(self.__name)

        self.__displayinfo()
    def __displayinfo(self):
        print("welcome to india")

obj=Student()


# Polymorphism

l=[10,20,30,40]
print(len(l))
s="welcome"
print(len(s))

# 1 overloading

class A:
    def displayinfo(self,name=''):
        print("welcome "+name)
obj=A()
obj.displayinfo()
obj.displayinfo('python')

# 2 overiding
#super - with the help of super() parentfunction call inside
class A:
    def displayinfo(self):
        print("welcome ")
class IIT(A):
     def displayinfo(self):
        super().displayinfo()
        print("welcome to IIT")
obj=IIT()
obj.displayinfo()


class A:
    def showData(self):
        print("I am in A class ")
class B(A):
    def showData(self):
        super().showData()
        print("I am in B class")
obj=B()
obj.showData()

# OVERLOADING
class Area:
    def find_area(self,x=None,y=None):
        if x!=None and y!=None:
            print(x*y)
        elif x!=None:
            print(x*x)
        else:
            print("Nothing")
obj=Area()
obj.find_area()
obj.find_area(10)
obj.find_area(10,20)

