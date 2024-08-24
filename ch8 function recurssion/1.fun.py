# marks = [45, 78, 86, 77]
# percentage1 = ((marks[0] + marks[1] + marks[2] + marks[3]) /400)*100

# marks2 = [75, 98, 88, 76]
# percentage2 = ((marks2[0] + marks2[1] + marks2[2] + marks2[3] )/400)*100
# print(percentage1, percentage2)

# 2nd method

# def percent(marks):
#     p = ((marks[0] + marks[1] + marks[2] + marks[3])/400)*100
#     return p

# marks1 = [40, 45, 86, 77]
# percentage1 = percent(marks1) 

# marks2 = [75, 98, 88, 55]
# percentage2 = percent(marks2)
# print(percentage1, percentage2)


def factorial(n):
    if(n==0 or n==1):
       return 1
    else:
       return n*factorial(n-1)
print(factorial(5))




def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]
 
 
s = "Geeksforgeeks"
 
print("The original string is : ", end="")
print(s)
 
print("The reversed string(using recursion) is : ", end="")
print(reverse(s))