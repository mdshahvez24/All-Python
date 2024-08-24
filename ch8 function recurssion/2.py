def greet(name):
    print("Good Day, "+ name)

greet("harry")

def mySum(num1, num2):
    return num1 + num2

s = mySum(6, 32)
print(s)


ch = "I\nLove\tGeeksforgeeks"
 
print ("The string without repr() is : ")
print (ch)
 
print ("\r")
 
print ("The string after using repr() is : ")
print (repr(ch))