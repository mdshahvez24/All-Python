#assignment operator

a = 10
b = 5
a += b  # or a = a+b
print(a)

# comparison operator 
a = 5
b = 2

print(a>b)  #true bcz 5 is greater than 2

# comparison operator

a = 5
b = 2

# equal to operator
print('a==b =',a==b)

#not equal to operator 
print('a !=b =', a !=b)

# Greater than 
print('a>b=', a>b)

# less than 
print('a<=b', a<=b)

# Greater than or equal to operator 
print('a>=b', a>=b)

#less than or equal to operator
print('a <= b =', a<=b)

#Logical operator 
a = 5
b = 6
print((a>2) and (b>=6))

# Membership operators

x = 'Hello world'
y = {1:'a', 2:'b'}

# check if 'H' is present in x string
print('H' in x)  # prints True

str= "hello"
print("h" in str)  # true
print("H" in str)  # false

# Identity operator 
x = 10
y = 10
print(x is y,x==y)   # True True
print (x is not y,x!=y)  # False False