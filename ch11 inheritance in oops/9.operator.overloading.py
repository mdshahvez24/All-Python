# Whenever you change the behavior of the existing operator through operator overloading, you have to redefine the special function that is invoked automatically when the operator is used with the objects. 

class A:
    def __init__(self, a):
        self.a = a

    # adding two objects 
    def __add__(self, o):
        return self.a + o.a

ob1= A(10)
ob2= A(20)
ob3= A("Ali")
ob4= A("Baba")

# print(ob1 + ob2)
# print(ob3 + ob4)

# Actual working when Binary Operator is used.
print(A.__add__(ob1,ob2)) 
print(A.__add__(ob3,ob4)) 

print(ob1.__add__(ob2))
print(ob3.__add__(ob4))

# 2nd
class A:
    def __init__(self, a):
        self.a = a
    def __gt__(self, other):
        if(self.a>other.a):
            return True
        else:
            return False
ob1 = A(2)
ob2 = A(3)
if(ob1>ob2):
    print("ob1 is greater than ob2")
else:
    print("ob2 is greater than ob1")

# overloading 

class Area:
    def find_area(self, x=None,y=None):
        if x!=None and y!=None:
            print(x*y)

        elif x!=None:
            print(x*x)
        else:
            print("Nothing")

obj1 = Area()
obj1.find_area()
# obj1.find_area(10) #  100
obj1.find_area(10,20)


class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"

    def __add__(self, x):
       return f"{self.i + x.i}i + {self.j + x.j}j + {self.k + x.k}k"

v1 = Vector(3, 5, 6)
print(v1)
v2 = Vector(1, 2, 3)
print(v2)
print(v1+v2)


class A:
    def __init__(self,a):
        self.a = a
    def __lt__(self, other):
        if(self.a<other.a):
            return "ob1 is less than ob2"
        else:
            return "ob2 is less than ob1"
    def __eq__(self, other):
        if(self.a == other.a):
            return "both are equal"
        else:
            return "not equal"
          

ob1 = A(2)
ob2 = A(3)
print(ob1 < ob2)
ob3 = A(4)
ob4 = A(4)
print(ob1 == ob2)

#  overriding single in heritance

class A:
    def showdata(self):
        print("I am in A class")

class B(A):
    def showdata(self):
        print("I am in B class")

obj = B()
obj.showdata()
