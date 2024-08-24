
list = [['Harry', 40], ['Berry', 39.5], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39.5]]

# for i in list:
#     print(i[0])

# list comperehension
findScore = [i[1] for i in list]
print (findScore)
sortScore = sorted(set(findScore))
# print(sortScore)    #  [37.2, 39.5, 40, 41]
print(sortScore[1])

# for j in list:
#     if(sortScore[1]== j[1]):
#         print(j[0])

findName = sorted([j[0] for j in list if(sortScore[1] == j[1])])
# print(findName)
for z in findName:
    print(z)
