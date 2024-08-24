# WAP to enter marks of 6 student in sorted manner

m1 = int(input("enter the marks of student 1 "))
m2 = int(input("enter the marks of student 2 "))
m3 = int(input("enter the marks of student 3 "))
m4 = int(input("enter the marks of student 4 "))
m5 = int(input("enter the marks of student 5 "))
m6 = int(input("enter the marks of student 6 "))

myList = [m1, m2, m3, m4, m5, m6]
myList.sort()
print(myList)

# wap to  tuple chnge test
a = (2,4,5,3,2)
a[0] = 45
print(a)