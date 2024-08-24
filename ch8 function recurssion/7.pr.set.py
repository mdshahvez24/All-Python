# wap to print first n line of the pattern
n = 3
for i in range(n):
    print("*" * (n-i))


# WAP converts inches to cm

def inch_to_cm(n):
    print("length in cm:", n * 2.54)

num = 2

inch_to_cm(num)

    

#write a function to remove word from a string and strip it at the same time

def remove_and_split(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()

this = "    Harry is good    "
n = remove_and_split(this, "Harry")
print(n)
# # print(this)
# # print(this.strip())


