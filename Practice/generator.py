# Generate the value on the fly
# creating a generator

def my_generator():
    for i in range(10):
        yield i

gen = my_generator()

# print(next(gen))  0
# print(next(gen))  1
# print(next(gen))  2

for j in gen:
    print(j)