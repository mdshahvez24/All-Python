# write a class calculator capable of finding square cube and square root of a number

class Calculator:
    def __init__(self, num):    # num is an argument
        self.number = num

    def square(self):
        print(f"the value of {self.number} square is {self.number **2}")
    def squareRoot(self):
        print(f"the value of {self.number} square is {self.number **0.5}")
    def cube(self):
        print(f"the value of {self.number} square is {self.number **3}")

a = Calculator(3)
a.square()
a.squareRoot()
a.cube()