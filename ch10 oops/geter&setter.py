#Accessor Method is a getter method 
#Mutuator Methid is  a setter method

# getter - thius method read access 
class Mobile():
   def __init__(self):
      self.model = 'realme X' # instance variable

   def get_model(self):
      return self.model    

realme = Mobile()
m = realme.get_model()
print(m)    #   realme X

# setter /mutuator - modify data

class Mobile():
   def __init__(self):
      self.model = 'realme X' # instance variable

   def set_model(self):   # mutuator
       self.model = 'Realme 2'   

realme = Mobile()
# Before setting 
print(realme.model)  
# After Setting
realme.set_model()
print(realme.model)

class Mobile():
    def set_model(self, m):   # mutuator
        self.model = m  
        
realme = Mobile()
realme.set_model('Realme XT')
print(realme.model)





class Student:
    def __init__(self):
        self.__name=""
    def getname(self):
        return self.__name
    def setname(self,name):
        self.__name=name
    
obj=Student()
obj.setname("Testing")
name=obj.getname()
print(name)


