# function is a block of statement which can be used repetitively in a program.it save time 
# user define function
# 1.simple function
# 2.function with argument
# 3.return type

def showdata():
    print("welcome to tcs")
showdata()
showdata()

def sumdata(a,b):
    print(a+b)
sumdata(10,25)   # 35

def sumdata(a,b):
    print(a+b)
sumdata(5,10)   # 65

# Default parameter value
def sumdata(a,b=5):
    print(a+b)
sumdata(20)     #  25

def sumdata(a,b=1):
    print(a+b)
sumdata(20)     #  25
sumdata(40,20)     #  25

# Return values
def square(x):
    return x*x,x*2
s=square(5)
print(s)

def add(x,y):
    return x+y
a=add(10,20)
print(a)
