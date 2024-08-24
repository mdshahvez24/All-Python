# c =11         #     global variable
# def add():
#     print(c)
# add()

#  global variable

c = 11      
def add():
    global c  #gloabal keyword
    #increment c by 2
    c= c + 2

    print(c)
add()

# upper program show an error  local variable 'c' referenced before assignment
#global c