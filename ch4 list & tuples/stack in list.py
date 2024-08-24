#  stack -- the stack is linear data structure
# stroe item in a list-in/first out (LIFO) or FILO first in last out .
                                            #  stack 
# 1.push -- insertin an element                 _____
                                            #  |__4__|
                                            #  |__3__|
                                            #  |__2__|
                                            #  |__1__|
                                            #  |__0__|

l=[]
while True:
    c = int(input('''
           1 Push elements
           2 Pop elements
           3 Peek element
           4 Display stack
           5 Exit 
           '''))

    if c==1:
        n=input("enter the value:-")
        l.append(n)
        print(l)
    if c==2:
        if len(l)==0:
            print("empty stack")
        else:
            p=l.pop()
            print(p)
            print(l)
    elif c==3:
        if len(l)==0:
            print("empty stack")
        else:
            print("Last stack Value:-",l[-1])
    elif c==4:
        print("Display stack",l)
    elif c==5:
        break
    else:
        print("Invalid choice")

# Queue -- it is linear data structure
#  store item in first in first out(FIFO) manner.
#                 Rear                              front
            #    ___^_________________________________^__
            #    |__7_|__6__|__5__|__4__|__3__|__2__|___|--> 1
                                            
l=[]
while True:
    c = int(input('''
           1 Push elements
           2 Pop first elements
           3 Front element
           4 Last element
           5 Display Queue
           6 Exit 
           '''))

    if c==1:
        n=input("enter the value:-")
        l.append(n)
        print(l)
    if c==2:
        if len(l)==0:
            print("empty Queue")
        else:
            del l[0]
            print(l)
    elif c==3:
        if len(l)==0:
            print("empty Queue")
        else:
            print("First Queue Value:-",l[0])
    elif c==4:
        if len(l)==0:
            print("empty Queue")
        else:
            print("Last Queue Value:-",l[-1])

    elif c==5:
        print("Dispaly Queue",l)
    elif c==6:
        break
    else:
        print("Invalid choice")
                                             
                                             