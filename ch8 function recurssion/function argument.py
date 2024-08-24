
# def add_numbers(a, b):
#     sum = a + b
#     print('Sum:', sum)

# add_numbers(2, 3)

# # Output: Sum: 5

# def add_numbers( a = 7,  b = 8):
#     sum = a + b
#     print('Sum:', sum)

# #  function call with one argument 
# add_numbers(a = 2)  # 10

# # function call with no arguments
# add_numbers()

# program to find sum of multiple numbers 

def find_sum(*numbers): # * use for multiple arguments
    result = 0
    
    for num in numbers:
        result = result + num
    
    print("Sum = ", result)

# function call with 3 arguments
find_sum(1, 2, 3)

# function call with 2 arguments
find_sum(4, 9)