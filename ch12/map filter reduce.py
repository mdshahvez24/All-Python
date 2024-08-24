def cube(x):
    return x*x*x

# Map
print(cube(2))

l = [1,2,3,4,5]
newl = list(map(lambda x: x*x*x, l))
print(newl)          #[1, 8, 27, 64, 125]
newl = list(map(cube, l))

#filter 
l = [1,2,3,4,5,6,7,8,2]
def filter_function(a):
    return a>5

newl = list(filter(filter_function, l))
print(newl)

#reduce function 

from functools import  reduce 
#List of no 
numbers  =[1,2,3,4,5]

# calculate the sum of a the no usong the reduce function
def mysum(x,y):
    return x+y
    return x*y
sum = reduce(mysum, numbers)

#Second way
sum = reduce(lambda x, y: x+y,numbers)

# print the sum
print(sum)