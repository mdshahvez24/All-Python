# # a = 7
# # b = 2

# # # addition
# # print ('Sum: ', a + b)  

# # # subtraction
# # print ('Subtraction: ', a - b)   

# # # multiplication
# # print ('Multiplication: ', a * b)  

# # # division
# # print ('Division: ', a / b) 

# # # floor division
# # print ('Floor Division: ', a // b)

# # # modulo
# # print ('Modulo: ', a % b)  

# # # a to the power b
# # print ('Power: ', a ** b)   

# # #assignment operator

# # a = 10
# # b = 5
# # a += b  # or a = a+b
# # print(a)


# # Enter your code here. Read input from STDIN. Print output to STDOUT
# import math
# a = int(input())
# b = int(input())
# m = int(input())
# c = math.pow(a, b)
# d = c%m
# print(int(c))
# print(int(d))/

L =[1,2,3,4,5,6]
print(L**2)

# operator

a,b =10,20
if a!=b:
    if a>b:
        print("a is greater than b")
    else:
        print("b is greater than a")
else:
    print("Both a and b are equal")

a, b = 10, 20
 
print ("Both a and b are equal" if a == b else "a is greater than b"
        if a > b else "b is greater than a")


# In this example, we are using tuples to demonstrate ternary operator. We are using tuple for selecting an item and if [a<b] is true it return 1, so element with 1 index will print else if [a<b] is false it return 0, so element with 0 index will print.

a, b = 10, 20
 
print( (b, a) [a < b] )

a=5
b=7
 
# [statement_on_True] if [condition] else [statement_on_false] 
print(a,"is greater") if (a>b) else print(b,"is Greater")