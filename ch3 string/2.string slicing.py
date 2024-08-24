# b = "harry's" #--> use this if you have a single Quotes in your string
# b = 'harry"s'   #  inerpreter look for closing quotes
# b = '''harry"s and harry's'''
# print(b)
# print(type(b))

# concatenating two string
 
# greeting = "gud morning"
# name = " harry"
# print(type(name))
# c = greeting +  name
# print(c)

# printing the string character
# name = "harry"
# print(name[4])

# name [3] = "d" we cant chnge the string charcter

# slicing of string
# name = "Harry"
# print(name[0:3])
# print(name[1:4])
# print(name[:4])  #Harr [0:4]
# print(name[0:]) #harry 
# print(name[1:]) #arry  [1:5]
# # print(name[-1]) #y
# c = name[-4:-1] #arr same as name [1:4]
# print(c)

# slicing with skip value
name = "abcdef"
d = name [1:5:2] # 1-5 with skip value 2 every second element should be skip
print(d)



ch = "I\nLove\tGeeksforgeeks"
 
print ("The string without repr() is : ")
print (ch)
 
print ("\r")
 
print ("The string after using repr() is : ")
print (repr(ch))