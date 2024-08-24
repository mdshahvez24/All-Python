a = 34
b = 'harry'
print(a, b)

# left to Right slicing
w = "ABCDEFGHIJKL"
print(w[6])  # G
print(w[-1])  # L
print(w[8])  # I
print(w[0:7])  # ABCDEFG
print(w[0::2])  # increment of 2

# Right to left slicing reverse slicing
w = "ABCDEFGHIJKL"
t=len(w)
print(t) # 12 length
for a in range(t):
    print(w[a])

print(w[-1::-2]) # LJHFSB
print(w[-1::-1]) # LKJIHGFEDCBA

# REVERSE STRING
w = "ABCDEFGHIJKL"
w=w[-1::-1] #LKJIHGFEDCBA
t=len(w)
print(t) 
for a in range(t):
    print(w[a])

#  2nd method
w = "ABCDEFGHIJKL"
t=len(w)
for a in range(t-1,-1,-1):
    print(w[a])

w = "ABCDEFGHIJKL"
for a in w:
    print(a)