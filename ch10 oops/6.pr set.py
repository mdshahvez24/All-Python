# write a class with a class attribute a; create an object from it and set a directly using object a = 0 does this change the class attribute

class Sample:
    a = "Harry"

obj = Sample()
obj.a = "vikky"
#Sample.a = "vikky"  #it chnge the class attribute
print(Sample.a)
print(obj.a)

# Add a static method in problem to greet the user with hello.

class Calculator:
    def __init__(self, num):    # num is an argument
        self.number = num

    def square(self):
        print(f"the value of {self.number} square is {self.number **2}")
    def squareRoot(self):
        print(f"the value of {self.number} square is {self.number **0.5}")
    def cube(self):
        print(f"the value of {self.number} square is {self.number **3}")
    @staticmethod
    def greet():
        print("****hello there welcome to the best calculator of the world*****")

a = Calculator(3)
a.square()
a.squareRoot()
a.cube()
a.greet()