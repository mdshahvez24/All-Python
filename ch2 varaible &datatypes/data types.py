# int
num1 = 5
print(num1, 'is of type', type(num1))  

#float
num2 = 5.42
print(num2, 'is of type', type(num2))   

num3 = 8+2j
print(num3, 'is of type', type(num3))  

 #complex
a = 5
print(a,type(a))  # int

#string
s = "string"
print(s,type(s)) #string

#List

List = [1,2.2,'bd',(4,6)]
List[3]=10
print(List,type(List))  #list mutable /changeable

#tuple
t =(10,20,"hello")
t(10)  # it a integer single value tuple not considerde
print(t,type(t))

#  Dictionary

d= {
'c_name':"python",
'id2':"122",
'id3':"123"}
print(d['id2'])
print(type(d))

myDict = {
    "Fast": "In a Quick Manner",
    "Harry": "A coder",
    "Marks":[1, 2, 3],
    "anotherdict": {'harry': 'Player'}
}

# print(myDict['Fast'])
# print(myDict['Harry'])

# myDict['Marks'] = [45, 78]
# print(myDict['Marks'])
print(myDict['anotherdict'])
print(myDict['anotherdict']['harry'])  

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
# print(c.pop(3))
# print(c.pop()) # remove a random element from set

# .clear(): empty the set 
c.clear()

# . union return a new set with all item from both set

set1 = {1,2,4,3,5,8} 
set2 = {5,6,7,8}
Un = set1.union(set2)
In = set1.intersection(set2)
# print(Un)
print(In)