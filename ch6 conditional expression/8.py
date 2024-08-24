#WAP which finds out whether a given name is present in a list or not.
names = ["harry", "shubham", "rohit", "rohan", "aditi"]
name = input("enter the name to check\n")
if name in names:
    print("your name is present in the list")
else:
    print("your name is not present in the list")