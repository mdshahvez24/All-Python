#WAP to input 8 unique no in a from user and display all the unique numbers
# num1 = int(input("enter the 1\n"))
# num2 = int(input("enter the 2\n"))
# num3 = int(input("enter the 3\n"))
# num4 = int(input("enter the 4\n"))
# num5 = int(input("enter the 5\n"))
# num6 = int(input("enter the 6\n"))
# num7 = int(input("enter the 7\n"))
# num8 = int(input("enter the 8\n"))

# set = {num1, num2, num3, num4, num5, num6, num7, num8}
# print(set)


# can have a set with 18 int and "18"(str) as a value in it

s = {18, "18", 18.5}
# print(s)

set2 = set()
set2.add(20)
set2.add(20.0) # this value take as repetitive value 20
set2.add("20")
print(set2)
print(len(set2)) #lenth is return 2 set2 bcz 20.0 considered as 20