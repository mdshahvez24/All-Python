#Random randint() method-- 
#  return a number between 5 & 10 (both include):

import random 
n=random.randint(2,8)
print(n)

#random.range(3,9) --
#returns a number between 3 (includes) and 9(not included)
n1=random.randrange(2,4)
print(n1)

#Random choice() method
# return a random element from a list
import random
l=[10,20,30,50,40]
lc=random.choice(l)
print(lc)

#random()
import random
r=random.random()
print(r)

import random
l=[10,20,30,50,40]
random.shuffle(l)
print(l)

u=random.uniform(3,9)
print(u)  # random float value