# Set- It is a collection of non repeatative element return sorted value

a = {1, 5, 4, 2, 1}
print(a)

a = {}  #this syntax will create an empty dictionary not a empty set
print(type(a))
print(a)

#An empty set can be created using the below syntax:
b = set()
print(type(b))
# print(b)

#creating an empty set and add element by using 
# .add()

c = set()
c.add(4)
c.add(2)
c.add(3)
c.add(4) # 4 is not added bcz set is collection of non repeatative element
# c.add([4, 5, 6]) # we cannot add list in a set 
c.add((4, 5, 6)) # we can add a tuple in a set
# c.add({4:5}) # we cannot add a dictionary in set
print(c)
# .len -length of the set
print(len(c))

# .remove()
c.remove(2) # remove 5 from set b
# c.remove(10) # throws an error trying to remove 15(which is not present in set)
print(c)

# .pop() - remove value from the set
print(c.pop(3))
print(c.pop()) # remove a random element from set

# .clear(): empty the set 
c.clear()

# . union return a new set with all item from both set

set1 = {1,2,4,3,5,8} 
set2 = {5,6,7,8}
Un = set1.union(set2)
In = set1.intersection(set2)
# print(Un)
print(In)

# Convert a list into set

l=[10,20,30]
s=set(l)
print(type(s)) # set
s.add(40)
s.add(50)
print(s)

# update ()
l=[10,90,80]
s={10,20,30,40,50}
s.update(l)
print(s)

# pop() - remove random any no from set work on index no

s.pop()
print(s)
print(s.pop()) # 40

# remove()
set={10,20,30,40,50}

print(set.pop())


set.remove(50)
print(set)

set.discard(20)
print(set)



set1 = set() 
print("Initial blank Set: ") 
print(set1) 
set1 = set("GeeksForGeeks") 
print("\nSet with the use of String: ") 
print(set1) 
set1 = set(["Geeks", "For", "Geeks"]) 
print("\nSet with the use of List: ") 
print(set1) 
set1 = set([1, 2, 'Geeks', 4, 'For', 6, 'Geeks']) 
print("\nSet with the use of Mixed Values") 
print(set1)