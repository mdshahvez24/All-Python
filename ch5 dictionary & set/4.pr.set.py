# WAP to make a dictionary of hindi word with value of english transaltion 

myDict = {
    "Pankha": "fan",
    "Dabba": "box",
    "anda": "egg",
    "vastu": "item"
}

# print("Option are ", myDict.keys())
a = input("enter the hindi word\n")
print("the meaning of your word is:", myDict[a])

#Below  line will not throw an error if key value is not present in the dictionary
# print("the meaning of your word is:", myDict.get(a))

