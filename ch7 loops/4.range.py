# Range function-- The range function in python is used   to generate a sequence of number

# for i in range(8): # print 0-8
# for i in range(1, 8):  # print 1-7
# for i in range(1, 8, 2): # print 1357 2nd element skip stepsize
    # print(i)



# for i in range(3):
#    print(i*i)     #print square of no

n = input("enter saal")
n = int(n)
def is_leap(n):

    if (n%400==0 and n%100!=0) or (n%4==0):
        leap = True
    else :
        leap = False
    return leap



#     if n % 400 == 0:
#         return True
#         if n % 100 == 0:
#             return False
#             if n % 4 == 0:
#                 return True
#             return False
#             print("is leap year", n)

