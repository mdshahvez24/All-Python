try:
    numerator = 10
    denominator = 0

    result = numerator/denominator

    print(result)
except:
    print("Error: Denominator cannot be 0.")

# Output: Error: Denominator cannot be 0. 


try:
    numerator = int(input("enter numerator"))
    denominator = int(input("enter denominator: "))

    result = numerator / denominator
    print(result)
except ZeroDivisionError:
    # code to run when exception occurs
    print("denominator cannot be 0.Please try agian.")
    print("Program ends")


#custom error
a = int(input("Enter any value between 5 and 9:-"))

if(a<5 or a>9):
   raise ValueError("Value should be between 5 and 9")












   # def some_func(array):
#     array = iter(array)
#     try
#     first = next(array)
#     except stopIteration
#         return True
#     return all(first == x for x in array)


    # class Square:
    #     def draw(self):
    #         print(f'inside Square::draw()')

    #         def resize(self):
    #             print(f'inside Square::resize()')
   
    # class Circle:
    #     def draw(self):
    #         print(f'inside Circle::draw()')

    #         def resize(self):
    #             print(f'inside Circle::resize()')

# document = (25455,'baram'(101,102,325),['sing', 'quizz'])
# document [-1].append('poetry')

# for line in lines:
#     f(lines)