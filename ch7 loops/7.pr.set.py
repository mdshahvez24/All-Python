# WAP to print multiplication table of a given number using for loop.

# num = int(input("Enter the no\n"))
# for i in range(1, 11):
#     print(str(num) + " X " + str(i) + "=" + str(i*num))
#     # print(f"{num}X{i}={num*i}")

# Using while loop 

num = int(input("enter the no"))
i = 1
while i<=10:
    print(f"{num} X {i} = {num*i} ")
    # print("yes" + str(i))
    i = i + 1

#WAP- To greet all the person name stored in a list l1 and with starts with S

# l1 = ["harry", "sohan", "sachin", "Rahul"]
# for name in l1:
#     if name.startswith("s"):
#         print("hello " + name)


# WAP To print a prime no

num = int(input("Enter the number: "))
prime = True

for i in range(2, num):
    if(num%i == 0):
        prime = False
        break
if prime:
    print("This number is Prime")
else:
    print("This number is not Prime")

