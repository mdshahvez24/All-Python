# Multi threading use to download or transfer data from server parallely it means multi tasking

import threading
import time

def func(seconds):
    print(f"sleep for {seconds} second")
    time.sleep(seconds)

time1 = time.perf_counter()
# this way take time 6 second
# func(1)
# func(2)
# func(3)

# time2 = time.perf_counter()
# print(time2-time1)

t1 = threading.Thread(target=func, args=[4])
t2 = threading.Thread(target=func, args=[2])
t3 = threading.Thread(target=func, args=[1])

#instantly run
t1.start()
t2.start()
t3.start()

#if we want to do wait
t1.join()
t2.join()
t3.join()

#claculate time it take 0.003 seconds
time2 = time.perf_counter()
print(time2-time1)