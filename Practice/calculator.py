def add(a, b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a / b


#         for i in range(0, n):
     
#         # inner loop to handle number of columns
#         # values changing acc. to outer loop
#         for j in range(0, i+1):
         
#             # printing stars
#             print("* ",end="")
      
#         # ending line after each row
#         print("\r")

# row = int(input("enter the no: "))
# for row in range(1,row+1):
#     # for j in range(1,i+1):
#         print("* " * row)
   
# for i in range(1,6):
#     print('* '*i)

# for i in range(5):
#     for j in range(i+1):
#         print("*",end='')

input = 8
for i in range(1,11):
    print(f'{input} x {i} = {input*i}')