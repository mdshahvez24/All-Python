# Find a maximum no to choose greater no. in 3 no

def maximum(num1, num2, num3):
    if (num1>num2):
        if(num1>num3):
            return num1
        else:
            return num3
    else:
        if(num2>num3):
             return num2
        else:
            return num3
        
m = maximum(13, 55, 2)
print("the value of the maximum is " + str(m))

# celsisus to farhanite
def farh(cel):
    return (cel *(9/5) + 32)
c = 0  #(5 ,10 ,20)
f = farh(c)
print("farheneit trmp is " + str(f))

#how do prevent a python print() function to print a new line at the end

print("hello", end="")
print("how", end=" ")
print("are", end=" ")
print("you", end=" ")