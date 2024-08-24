test_list1 = [1, 4, 5, 6, 5]
test_list2 = [3, 5, 7, 2, 5]
 
# using naive method to concat
for i in test_list2 :
    test_list1.append(i)
 
# Printing concatenated list
print ("Concatenated list using naive method : "+ str(test_list1))

# Initializing lists
test_list1 = [1, 4, 5, 6, 5]
test_list2 = [3, 5, 7, 2, 5]
 
# using list comprehension to concat
res_list = [y for x in [test_list1, test_list2] for y in x]
 
# Printing concatenated list
print ("Concatenated list using list comprehension: "
                                    + str(res_list))



# Initializing lists
test_list1 = [1, 4, 5, 6, 5]
test_list2 = [3, 5, 7, 2, 5]
 
# using * operator to concat
res_list = [*test_list1, *test_list2]
 
# Printing concatenated list
print ("Concatenated list using * operator : "+ str(res_list))                                    