#decclare global variable
message = 'hello'

def greet():
    print('local', message)

greet()
print('global', message)

#Global variable

message = "how are you?"
def greet():
    # global message  # by writing this we can chnge the global variable
    message ="how  you doing ?"
    print("message inside the function", message)

greet()
print("meaage outside function", message)
