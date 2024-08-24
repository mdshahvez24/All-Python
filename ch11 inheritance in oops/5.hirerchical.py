class Father:
    def showF(self):
        print("Father class Method")

class Son(Father):
    def showS(self):
        print("Son class Method")

class Daughter(Father):
    def showD(self):
        print("Daughter class Method")

s= Son()
s.showS()   # Son class Method
s.showF()    #Father class Method
# s.showD()  # error 

d= Daughter()
d.showD()

# with constructor

class Father:
    def __init__(self):
        print("Father class Constructor")
    def showF(self):
        print("Father class Method")

class Son(Father):
    def __init__(self):
        super().__init__()
        print("Son class Constructor")
    def showS(self):
        print("Son class Method")

class Daughter(Father):
    def __init__(self):
        print("Daughter class Constructor")
    def showD(self):
        print("Daughter class Method")

s= Son()  # Son class Constructor


d= Daughter() # daughter class constructor
d.showD()