# json -- (javascript object notation)
# It is manily used for storing and transferring data between the browser and the server.
# json is text written with javascript object notation
# Python too support json  with a built in pakage called json.

# JSON support mainly 6data types
# string, number, boolean, null, object, array

import json
d={
    'course_name':'Python',
    'fees':15000,
    'duration':'12 days'
}

f=json.dumps(d)
print(f)
print(type(f))

# convert json to python objects like dictionary list string
# json.loads()

import json
d='{"cname":"python","fees":15000,"duration":"12 months"}' #json data
x=json.loads(d)
print(x)
print(type(x))
for a in x:

    print(a) # we get all key
    print(a,x[a]) # we get all key and pair


# read and write json file
import json
file=open("user.json","r")
x=file.read()
finaldata=json.loads(x)
# print(finaldata)

for a in finaldata:
    print(a['age'])


# create a json file
import json 
user = {
    "name": "jhon",
    "age": 24,
    "lang":"python"
}
data = json.dumps(user)
file = open('engpy.json','a')
file.write(data)
file.close()