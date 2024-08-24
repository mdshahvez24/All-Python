a = 10
b = 2

print(a+b)  # 12
print(a-b)  # 8
print(a*b)  # 20
print(a%b)  # 0
print(a**b)  # 10*2
print(10**4)  # 10*10*10*10=10000

print(10//3) # 3.3333335
print(10/3) # 3


#Arthmetic operators
print("the value of 3+4 is", 3+4)
print("the value of 3-4 is", 3-4)
print("the value of 3*4 is", 3*4)
print("the value of 3/4 is", 3/4)


# Assignment operator
a = 34
a -= 10   # 24
b = 15
b += 5  # 20
print(a,b)

# comparrission operators
b = (10>12)
# b = (10<12)
# b = (10>=12)
# b = (10<=12)
b = (10==7)
# b = (10!=7)
print(b)

# logical operators
bool1 = True
bool2 = False
print("the value of bool1 and bool2 is", (bool1 and bool2))
print("the value of bool1 or bool2 is", (bool1 or bool2))
print("the value of bool1 not bool2 is", (not bool1))

# Bitwise operator (AND OR XOR)
x=10
y=8
print(bin(x))
print(bin(y))
print(bin(x&y),x&y) # AND &
print(bin(x|y),x|y)  # or |
print(bin(x|y),x|y)  # xor ^
