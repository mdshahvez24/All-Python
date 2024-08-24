def cube(x):
    return x*x*x

# Map
print(cube(2))

l = [1,2,3,4,5]
newl = list(map(lambda x: x*x*x, l))
print(newl)          #[1, 8, 27, 64, 125]
newl = list(map(cube, l))