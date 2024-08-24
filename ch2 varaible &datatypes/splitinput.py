# input().split(separator, maxsplit)

x, y = input("Enter two values: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)
 
 
# taking three inputs at a time
x, y, z = input("Enter three values: ").split()
print("Total number of students: ", x)
print("Number of boys is : ", y)
print("Number of girls is : ", z)

# taking two inputs at a time using format
a, b = input("Enter two values: ").split()
print("First number is {} and second number is {}".format(a, b))

# taking multiple inputs at a time 
# and type casting using list() function
x = list(map(int, input("Enter multiple values: ").split()))
print("List of students: ", x) # print a list


# taking multiple inputs at a time separated by comma
x = [int(x) for x in input("Enter multiple value: ").split(",")]
print("Number of list is: ", x) 