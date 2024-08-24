## IF ELIF 
per =int(input("Enter the value:-"))
if per>=60:
    print("frist division")
elif per>=48:
    print("second division")
elif per>=35:
    print("third division")
else:
    print("fail")


num1 = int(input("enter the value1:-"))
num2 = int(input("enter the value2:-"))
opr=input("Enter the opr.(+,-,*,/).")
if opr=="+":
    print(num1+num2)
elif opr=="-":
    print(num1-num2)
elif opr=="*":
    print(num1*num2)
elif opr=="/":
    print(num1/num2)
else:
    print("invalid oprator")








age = int(input("enter the age\n"))
if age>18:
    print("yes")
else:
    print("no")

# Logical operators (and, or, not )
# and - both condition  should be satisfied
age = int(input("enter the age\n"))
if(age>34 and age<56):
     print("you can work with us")

# Or - it need only one condition for satisfaction
if(age>34 or age<56):
    print("you can work with us")
else:
    print("u cant work with us")

