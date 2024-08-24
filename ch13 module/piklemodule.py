import pickle

# make a txt file 

l=[10,20,30,40]
file=open("writedata.txt","wb")
pickle.dump(l,file)
file.close()

import pickle

file=open("writedata.txt","rb")
l=pickle.load(file)
print(l)