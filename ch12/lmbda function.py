def appl(fx, value):
    return 6 + fx(value)

# double = lambda x: x*2
cube = lambda x: x*x*x
# avg = lambda x,y: (x+y)/2
print(appl(cube, 2))

print(double(2))
# print(cube(5))
print(avg(11,5))

# declare a lambda function
greet = lambda : print('Hello World')

#call lambda function
greet()

#lambda that accept one argument
greet_user = lambda name : print('hey there,', name)

#lambda call 
greet_user('delihat')

#filter() fuction
my_list = [1,2,3,4,5,6,7,8,9,10,11]

new_list = list(filter(lambda x: (x%2 == 0) ,my_list))

print(new_list)

my_list = [1,2,3,4,5,6,7,8,9,10,11]

new_list = list(map(lambda x: x ** 2 ,my_list))

print(new_list)