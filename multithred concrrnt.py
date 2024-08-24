import threading
import time
from concurrent.futures import ThreadPoolExecutor

# Indicates some task being done
def func(seconds):
  print(f"Sleeping for {seconds} seconds")
  time.sleep(seconds)
  return seconds

def main():
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
# time2 = time.perf_counter()
# print(time2-time1)

def poolingDemo():
  with ThreadPoolExecutor() as executor:
    # future1 = executor.submit(func, 3)
    # future2 = executor.submit(func, 2)
    # future3 = executor.submit(func, 4)
    # print(future1.result())
    # print(future2.result())
    # print(future3.result())
# poolingDemo()


# 2nd way for parallel downloading

    l = [3, 5, 1, 2]
    results = executor.map(func, l)
    for result in results:
      print(result)

poolingDemo()