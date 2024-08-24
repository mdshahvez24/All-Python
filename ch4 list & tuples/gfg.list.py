# use 'any' function on list 
list1 = []
list2 = []
 
# Index ranges from 1 to 10 to multiply
for i in range(1,11):
    list1.append(4*i) 
print(list1)
 
# Index to access the list2 is from 0 to 9
for i in range(0,10):
    list2.append(list1[i]%5==0)
print(list2)
print('See whether at least one number is divisible by 5 in list 1=>')
print(any(list2))



# importing operator module  
import operator 
  
# Initializing list 
li = [1, 5, 6, 7, 8] 
  
# printing original list  
print ("The original list is : ",end="") 
for i in range(0,len(li)): 
    print (li[i],end=" ") 
  
print ("\r") 
  
# using setitem() to assign 2,3,4 at 2nd,3rd and 4th index 
import operator 

li = [1, 5, 6, 7, 8] 
operator.setitem(li,slice(1,4),[2,3,4]) 
  
# printing modified list after setitem() 
print ("The modified list after setitem() is : ",end="") 
for i in range(0,len(li)): 
    print (li[i],end=" ") 
  
print ("\r") 
  
# using delitem() to delete value at 3rd and 4th index 

import operator 

li = [1, 5, 6, 7, 8] 
operator.delitem(li,slice(2,4)) 
  
# printing modified list after delitem() 
print ("The modified list after delitem() is : ",end="") 
for i in range(0,len(li)): 
    print (li[i],end=" ") 
  
print ("\r") 
  
# using getitem() to access 1st and 2nd element 
print ("The 1st and 2nd element of list is : ",end="") 
print (operator.getitem(li,slice(0,2))) 