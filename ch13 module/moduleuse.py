import modulefun as m
# print(modulefun.sum(10,20))
print(m.sum(10,20))   #30
print(m.mul(10,20))

# 2nd method

from modulefun import sum
print(sum(10,20))  #30

from modulefun import *
print(sum(10,20))  #30
print(mul(10,20))  #200

