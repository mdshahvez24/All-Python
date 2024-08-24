# how does print function work 
name = "ali"
age = 25
# print(name,age)
print("hy my name is",name,"and i am",age,"years old")

print("gfg is wonderful" +'website')

a,b,=10,1000
print('The value of a is {} and b is {}'.format(a,b))


n = input('Enter the Number: ')
print('Number Entered by User:',n)

import time
 
count_seconds = 3
for i in reversed(range(count_seconds + 1)):
    if i > 0:
        print(i, end='>>>')
        time.sleep(1)
    else:
        print('Start')

import time

count_seconds=3
for i in reversed(range(count_seconds+1)):
    if i > 0:
        print(i,end='>>>',flush = True)
        time.sleep(1)
    else:
        print('start')


a=12
b=12
c=2022
print(a,b,c,sep="-")


import io
 
# declare a dummy file
dummy_file = io.StringIO()
 
# add message to the dummy file
print('Hello Geeks!!', file=dummy_file)
 
# get the value from dummy file
print(dummy_file.getvalue())

# Print without newline in Python 3.x without using for loop
 
l = [1, 2, 3, 4, 5, 6]
 
# using * symbol prints the list
# elements in a single 

# printing to statement in a single line with end='' space
print("Welcome to", end = ' ')
print("Welcome to", end = ' #')
print("GeeksforGeeks", end= ' ')

name = "Alice"
age = 30
print("My name is", name, "and I am", age, "years old.", end=" ")
print("Nice to meet you!")