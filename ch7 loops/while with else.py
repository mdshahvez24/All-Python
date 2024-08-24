# counter = 0 
# while counter < 3:
#     print('Inside loop')
#     counter = counter + 1
# else:
#     print('Inside else')


counter = 0

while counter < 3:
    # loop ends because of break
    # the else part is not executed 
    if counter == 1:
        
        break

    print('Inside loop')
    counter = counter + 1
else:      # this else block will not execute  if while loop terminate by else
    print('Inside else')

