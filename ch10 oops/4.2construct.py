class A:
    a=10
# constructor -it is a  method which call automatically
    def __init__(self):
        print("wscubetech ")

    def showvalue(self):
        self.b=self.a*self.a
        print(self.b) #100
    
    def show(self,c,d):
        print(c+d)

obj=A()
obj.showvalue()
obj.show(10,30)



class Person:
    def __init__(self, n, o):  # costructor
       print("Hey i am a person")
       self.name = n
       self.occ = o

    def info(self):
       print(f"{self.name} is a {self.occ}")

a = Person ("Harry", "Devloper")
b = Person ("Divya", "HR")
# c = Person ()
a.info()
b.info()



class Mob():
   def __init__(self):
      self.model = 'realme C'
   def show_model(self):
      print("Model:", self.model)

real = Mob()
real.show_model()
real.model = "Xt"
real.show_model()


class Mobile():
   def __init__(self):
      self.model = 'realme X' # instance variable

   def show_model(self):
      print(self.model)  # Accessing Instance Variable

realme = Mobile()
print(realme.model) # realme X

