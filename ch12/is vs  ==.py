# is compare the  identity of object

a=[1,2,33]
b=[1,2,33]

print(a is b) #exact loacation  of object in memory
print(a==b) # value 

a=[1,2,33]
b=[1,2,33]

print(a is b) #False
print(a==b) # True

a=4
b="4"
print(a is b) #False
print(a==b) # False 

a=3
b=3
print(a is b) #True 
print(a==b) # true


list1 = []
list2 = []
list3 = list1
 
# case 1
if (list1 == list2):
    print("True")
else:
    print("False")
 
# case 2
if (list1 is list2):
    print("True")
else:
    print("False")
 
# case 3
if (list1 is list3):
    print("True")
else:    
    print("False")
     
# case 4
list3 = list3 + list2
 
if (list1 is list3):
    print("True")
else:    
    print("False")




    def overlapping(list1, list2):
 
    c = 0
    d = 0
    for i in list1:
        c += 1
    for i in list2:
        d += 1
    for i in range(0, c):
        for j in range(0, d):
            if(list1[i] == list2[j]):
                return 1
    return 0
 
 
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9]
if(overlapping(list1, list2)):
    print("overlapping")
else:
    print("not overlapping")