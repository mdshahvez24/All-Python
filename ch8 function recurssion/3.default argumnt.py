def greet(name="Stranger"):
    print("Good Day, "+ name)
 

# greet("Harry") 
greet()


def add(x,y):
    c= x+y 
    print(c)

add(5,4)


def add_sub(x,y):
    c = x+y
    d = x*y
    return c,d

result1,result2 = add_sub(5,3)
print(result1,result2)



def driveStatus():
    age = 21
    if (age > 18): 
        print('you can drive')
    else:
        print('you can not drive')
driveStatus()