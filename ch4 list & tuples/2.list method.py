l =[]
for a in range(1,10):
    l.append(a)
print(l)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

n=[m for m in range(1,101)]
print(n) #[1-100]

n=[m for m in range(1,101) if m%2==0 ]
print(n)  # [2 4 6 8 10 12 14]

s="hello"
d=[a for a in s]
print(d)  ['h', 'e', 'l', 'l', 'o']

# l.sort()     sorts the list
l = [1, 8, 7, 2, 21, 15]   #print in a sorted or assending order
l.sort()      # real l sort real list 
print(l)


# reverse() the list
l = [1, 8, 7, 2, 21, 15] 
l.reverse()   # reverse the list
print(l)

#Append() at the end of list
l = [1, 8, 7, 2, 21, 15] 
l.append(45)   # adds at the end of list
print(l)

#l.insert()
l = [1, 8, 7, 2, 21, 15] 
l.insert(2, 54)   #insert 544 at index 2
print(l)
 
 #l.pop()  delete element 
l = [1, 8, 7, 2, 21, 15] 
print(l.pop(2)) #delete element at index 2
print(l)
#l.remove()
l.remove(21)   #remove 21 from the list 
print(l)

# count() how many time a value occur
l=[10,20,30,10,50,10]
c=l.count(10)
print(c)  #  3

m=max(l)
print(m) # 50

l=["hello", "world"]
m=min(l)
print(m) # hello


# Zip Function iterate 2 list at same time but length are should be same in both list
l=[10,20,30,50]
l1=[1,2,3,4]
t=len(l)

# with zip function
for a,b in zip(l,l1):
    print(a,b)

# without zip function
for i in range(t):
    print(l[i],l1[i])
    

# split() -- convert a string into list
n = input("Enter the value")
print(n)

l=n.split()
print(l)   #['Welcome', 'to', 'Ali', 'Baba']

#string to list
l =[]
for i in range(1,5):
    n = input("enter the value "+str(i)+":-")
    l.append(n)
print(l)  #['a', 'b', 'c', 'd']

