def swapList(newList):
    size = len(newList)

    temp = newList[0]
    newList[0] = newList[size-1]
    newList[size-1] = temp
    return newList

newList=[12,33,9,56,24]
print(swapList(newList))

def swapList(newList):
     
    newList[0], newList[-1] = newList[-1], newList[0]
 
    return newList
     
# Driver code
newList = [12, 35, 9, 56, 24]
print(swapList(newList))


#revrse a list 

def Reverse(lst):
   new_lst = lst[::-1]
   return new_lst
 
 
lst = [10, 11, 12, 13, 14, 15]
print(Reverse(lst))

lst = [10, 11, 12, 13, 14, 15]
lst.reverse()
print("Using reverse() ", lst)
 
print("Using reversed() ", list(reversed(lst)))



original_list = [10, 11, 12, 13, 14, 15]
new_list = [original_list[len(original_list) - i]
            for i in range(1, len(original_list)+1)]
print(new_list)