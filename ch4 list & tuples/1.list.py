a = [10, 20, 30, 40, 50 ,60]

# print the list using print() function
print(a)

# Access using index using a[0], a[1], a[2]
print(a[2])    #30
print(a[3:])   #40, 50, 60
print(a[2],a[3])   # 20 30
print(a[0::2])     #[10,30,50]
print(a[-1::-1])   #[60, 50, 40, 30, 20, 10]
# change the value of list using
a[0] = 5
print(a)

# we can create the list with item of different types
c = [45, "harry", False, 6.9]
c[2]=50
print(c) # [45, 'harry', 50, 6.9]

# list slicing
friends = ["harry", "tom", "rohan","sam", "divya", 45]
print(friends[0:4])
print(friends[-4:])    #['rohan', 'sam', 'divya', 45]
print(friends[-1:])    # 45
print(friends[0::2])   #['harry', 'rohan', 'divya']
print(friends[-1::-1])   #[45, 'divya', 'sam', 'rohan', 'tom', 'harry']


l=[10,20,30,40,50]
t=len(l)
print(t)   # 5

for a in range(t-1,-1,-1):
    print(l[a])  # 50 40  30 20 10 

for a in range(t):
    print(l[a])

for a in l:
    print(a) #  10 20 30 40 50


