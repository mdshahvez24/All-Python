with open('another.txt','w') as f:
    f.write('hello world3')
    f.truncate(5)

with open('another.txt','r') as f:
    print(f.read())