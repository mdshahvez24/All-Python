# addition of string and integer using explicit converision
num_string = '12'
num_integer = 23

print("data type of num_string brfore type casting", type(num_string))

num_string = int(num_string) #explict type conversion of num string
print("data type of num_string after type casting",type(num_string))

num_sum = num_integer + num_string

print("sum:", num_sum)
print("Data type of num_sum", type(num_sum))