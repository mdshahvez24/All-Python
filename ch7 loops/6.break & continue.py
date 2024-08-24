# Break statement- we can stop the loop before it has looped through all items:

for i in range(10):
    print(i)
    if i == 5:
        break
    # else:
    #     print("Done")

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")


# Continue -statement -- we can stop the current iteration of the loop and continue with the next

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

  
for i in range(10):
    if i == 5:
       continue  # it will skip 5 and continue to 9
    print(i)

# Pass -statement : Do nothing it is null statement no content, put in the pass statement

l = [1, 2, 3]
for item in l:
  pass # without pass it will throw an error