# Dunder method are specially method that you can define in your class and when invoked  __len__

class  Employee:
    name = "harry"
    def __len__(self):
        i= 0
        for c in self.name:
           i = i+1
        return i

e = Employee()
print(e.name)
print(len(e))


class Emp:
    name = "harry"
    def __len__(self):
        return self.name

e = Emp()
print(e.name)


class Fruits:
    def __init__(self, name):
        self.name = name

    def __mul__(self, other):
        return self.name * other

fruit = Fruits('Banana ')
print(fruit * 4)  # it was called indirectly because of multiplication operator



class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, num2):
        print("Lets add")
        return self.num + num2.num #  10
    
    def __mul__(self, num2):
        print("Lets mul")
        return self.num * num2.num  #  24

    def __str__(self):
        return f"Decimal Number: {self.num}"
    
    # def __len__(self):
    #     return 1
    
n = Number(9)
print(n + n)  #18
print(n * n)  #81


print(len(n))