# function caching is a technique for improveing the performance of a program by storing the result of a function call so that you can reuse  the result insted of recomputing it is mostly use for repeatation

import functools
import time

@functools.lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return n*5

print(fx(20))
print("done for 20")
print(fx(2))
print("done for 2")
print(fx(6))
print("done for 6")

# this part of code execute faster than upr
# this is because of lru_cache it fetch the old result for same calculation
print(fx(20))
print("done for 20")
print(fx(2))
print("done for 2")
print(fx(6))
print("done for 6")

# slow computation
print(fx(61))
print("done for 61")
print(fx(62))
print("done for 62")
