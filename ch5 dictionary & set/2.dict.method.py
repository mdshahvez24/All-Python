d={
    'key': 'value',
    'name': 'ali',
    'fees': 4500,
    'duration':'2 months'
}
c=d.get('key')
print(c)  # value 

c1=d['key']
print(c1) # value

# .keys() -- get all keys
for i in d.keys():   # key name fees duration
    print(i)         

# .value -- get al values
for i in d.values():
    print(i)   #ali 4500 2 months

# .items return both key and value
for a,b in d.items():
    print(a,b) 

# del keyword and .pop
del d['key']
print(d)

print(d.pop('duration'))
print(d)

# .update()
d.update({'fees':'10000'})
print(d)

d['desc']="this is java"
print(d)

#.clear -- clear list
d.clear()
print(d)


# Creating a dictionary
d=dict(name='python',fees=800)
print(d)  #  {}


#   Nested dictionary 
course = {
    'php':{'duration':'2 months','fees':'15000'},
    'java':{'duration':'4 months','fees':'25000'},
    'python':{'duration':'3 months','fees':'20000'}
}

course['java']['fees']=50000  # updatae java fees 
print(course)
print(course['php'])
print(course['php']['fees'])


for a,b in course.items():
    print(a,b)
    print(a,b['duration'],b['fees'])


myDict = {
    "fast": "in a quick manner",
    "harry": "a coder",
    "marks": [1,2,5],
    "anotherdict": {'harry': 'player'},
    1: 2
}
# Dictionary methods

# myDict.keys/values
print(list(myDict.keys()))  # print the key  of the dictionary
print(list(myDict.values())) # print the values of dictionary

# .item()
print((myDict.items())) # print the (key values)for all content of dictionary

# # .Update()
updateDict = {
    "lavish": "friend",
    "harry": "a dancer"
}
# myDict.update(updateDict) #update the dictionary by adding key value pair from updateDict
# print(myDict)

# # .get()

print(myDict.get("harry"))  #print value assosiated with key harry 

# print(myDict["harry"]) # print value assosiated with key harry

# # the difference b/w .get and [] syntax in dictionary ?
# print(myDict.get("harry2"))  # return none as harry2 not present in dictionary
# print(myDict["harry2"]) #throw an error as harry2 is not present in the dictionary
