# write a recursive function to calculate the sum of first n natural no

def recur_sum(n):
        if n<=1:
            return n
        else:
            return n + recur_sum(n-1)
        
num = 10

if num < 0:
    print("enter a positive no")
else:
    print("the sum is ")

s =  recur_sum((num))
print(s)

