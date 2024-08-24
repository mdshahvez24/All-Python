# WAP to sum of N natural no
# num = int(input("Enter the number:\n"))
# sum = 0
# i = 1
# while i<=num:
#     sum = sum + i
#     i = i+1
    
# print("the sum of  natural no is",sum)

#WAP to find the factorial of a no

    # n! = 1 X 2 X 3 X ..... X n
# 5! = 1 X 2 X 3 X 4 X 5

num = int(input("Enter the number: "))
factorial = 1
for i in range(1, num+1):
    factorial = factorial * i
print(f"The factorial of {num} is {factorial}")