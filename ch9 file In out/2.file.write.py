f = open('another.txt','r')
i = 0
while True:
    i = i + 1
    line= f.readline()
    if not line:
        break
    m1 = line.split(",")[1]
    m2 = line.split(",")[2]
    m3 = line.split(",")[3]
    print(f"Marks of student {i}  in maths is: {m1} ")
    print(f"marks of student {i} in sst is :{m2}")
    print(f"marks of student {i} in sst is: {m3}")

    print(line)

f = open('another.txt', 'r')
i = 0
while True:
  i = i + 1
  line = f.readline()
  if not line:
    break
  m1 = int(line.split(",")[0])
  m2 = int(line.split(",")[1])
  m3 = int(line.split(",")[2])
  print(f"Marks of student {i} in Maths is: {m1*2}")
  print(f"Marks of student {i} in English is: {m2*2}")
  print(f"Marks of student {i} in SST is: {m3*2}")

  print(line)


    
# f.write("likh do file mai file")
# # f.write("I am appending")
# f.close()








# f = open('another.txt','w')
# f.write("likh do file mai file")
# # f.write("I am appending")
# f.close()
