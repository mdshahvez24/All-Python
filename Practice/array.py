import array as arr
arr=(10,20,30,40)
print(a)

from array import *
vals = array('i',[5,9,8,4,2])
newArr = array(vals.typecode, (a*a for a in vals))
for e in newArr:
    print(e)

arr = array('i',[])
n= int(input("enter the value of array"))

for i in range(5):
    x = int(input("Enter thhe next value"))
    arr.append(x)
print(arr)