with open('another.txt','r') as f:
    print(type(f))

# seek() start read after 10  byte
    f.seek(10)
# tell function read the current position of the bites

    print(f.tell()) 
    data = f.read(5)
    print(data)

with open('another.txt','w') as f:
    f.write('hello world3')
    f.truncate(5) # hello

with open('another.txt','r') as f:
    print(f.read())

