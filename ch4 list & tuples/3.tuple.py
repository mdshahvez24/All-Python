# creating a tuple using ()
t = (1 ,2, 3, 4, 5)
# t1 = (1)  #wrong way to declare a tuple with single element
t1 = (1,) #tuple with single element
print(t1)
print(t)
print(type(t))

# printing the element of a tuple
# print(t[0])

# cannot update the value of tuple 
# t[0] = 34 # throws an error

# min and max-- minimum vaulue
t = (10 ,20, 30, 40, 50,20)
m=min(t)
ma=max(t)
print(m)   #  10
print(ma)  #  50

l=len(t)

for i in range(l):
    print(t)

# count -- how many time a no occur
c=t.count(20)
print(c)  # 20

#index()
c=t.index(40)
print(c)  # 

#sum
s=sum(t)
print(s)  # 170

Tuple1 = () 
print("Initial empty Tuple: ") 
print(Tuple1) 
Tuple1 = ('Geeks', 'For') 
print("\nTuple with the use of String: ") 
print(Tuple1) 
list1 = [1, 2, 4, 5, 6] 
print("\nTuple using List: ") 
print(tuple(list1)) 
Tuple1 = tuple('Geeks') 
print("\nTuple with the use of function: ") 
print(Tuple1) 
Tuple1 = (0, 1, 2, 3) 
Tuple2 = ('python', 'geek') 
Tuple3 = (Tuple1, Tuple2) 
print("\nTuple with nested tuples: ") 
print(Tuple3)
