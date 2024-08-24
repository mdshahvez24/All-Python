class Father:
    def showF(self):
        print("Father class Method")

class Son(Father):
    def showS(self):
        print("Son class Method")

class Gson(Son):
    def showG(self):
        print("Gson class Method")

g = Gson()
g.showG()
g.showF()
g.showS()

# With constructor 
# constructor call with a object creation

class Father:
    def __init__(self):
        print("Father class Constructor")
    def showF(self):
        print("Father class Method")

class Son(Father):
    def __init__(self):
        print("Son class Constructor")
    def showS(self):
        print("Son class Method")

class Gson(Son):
    def __init__(self):
        print("Gson class Constructor")
    def showG(self):
        print("Gson class Method")

g = Gson()  #Gson class Constructor
# g.showG()
# g.showF()
# g.showS()


# when we call son constructor we can use super()

class Father:
    def __init__(self):
        print("Father class Constructor")
    def showF(self):
        print("Father class Method")

class Son(Father):
    def __init__(self):
        print("Son class Constructor")
    def showS(self):
        print("Son class Method")

class Gson(Son):
    def __init__(self):
        super().__init__()  # calling son class constructor
        print("Gson class Constructor")
    def showG(self):
        print("Gson class Method")

g = Gson()  # Gson class Constructor 
            #son class construtot
# g.showG()
# g.showF()
# g.showS()



# class Employee:
#     company = "visa"
#     eCode = 120

class Freelancer:
    company = "Fiverr"
    level = 0

    def upgradeLevel(self):
        self.level = self.level + 1

class Employee:
    company = "visa"
    eCode = 120

# class Programmer(Freelancer, Employee): # priority given which class write first
# class Programmer(Employee, Freelancer):
class Programmer(Freelancer,Employee):
    
     
    name = "Rohit"

p = Programmer()
p.upgradeLevel()
print(p.level)
print(p.company)