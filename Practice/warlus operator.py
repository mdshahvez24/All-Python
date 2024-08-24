#Warlus operator is a new addition to python 3.8 and  allow you to assign a value to variable within a expression this can be useful when you need to use a value multiple times ina loop

a = True 
print(a:=False)  # False

numbers = [1,2,3,4,5]

while (n:= len(numbers)) > 0:
    print(numbers.pop())


# food = list()
# while True:
#     food = input("what food do you like?: ")
#     if food =="quit":
#         break
#     food.append(food)


foods = list()
while (food := input("what food do u like ?:")) != "quit":
    food.append(food)