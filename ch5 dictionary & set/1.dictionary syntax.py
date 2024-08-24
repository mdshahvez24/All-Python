#  Dictionary A dictionary is a collection which is unorderd .in python dictionaries are written with curly bracket{}  .it is a key value pair

d={
    'key': 'value'
    'name': 'ali',
    'fees': 4500,
    'duration':'2 months'
}
f=d['fees']
print(f)       # 4500

# iteration of dictionary

for i in d:
    print(d[i])  # value ali 4500 2 monts


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