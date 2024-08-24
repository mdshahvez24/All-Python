import random
Cnumber=random.randrange(1,101)
userInput=int(input("Enter your no:--"))
if userInput>Cnumber:
    print("Computer no",Cnumber)
    print("Your guess number is to high then computer")
elif Cnumber>userInput:
    print("Computer no",Cnumber)
    print("Your guess number is to low then computer")
else:
    print("Computer no",Cnumber)
    print("your guess no is equal")

