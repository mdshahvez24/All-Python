import time

# get time of execution of loop

initial = time.time()
k = 0
while(k<5):
    print("this is time")
    k+=1
print("while loop ran in", time.time()-initial, "second")

initial2 = time.time()
for i in range(5):
    print("this is harry")
print("for loop ran in", time.time()-initial2, "second")


import time

localtime = time.asctime(time.localtime(time.time()))
print(localtime)


# sleep() -- take time to run sleep for some second

import time

initial = time.time()
k = 0
while(k<5):
    print("ALi Baba")
    time.sleep(3)
    k+=1


# strftime()

import time
t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S",t)
print(formatted_time) # 2024-01-28 18:45:37