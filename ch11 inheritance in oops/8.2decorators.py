# decorators --thedecorator function which takes the original function as a argument and return a modified version of it .


def decorator_function(any_function):
    def wrapper_function():
        print("this is awsom function")
        any_function()
    return wrapper_function

@decorator_function
def func1():
    print("this is function 1")
# func1()

def func2():
    print("this is function 2")

var = decorator_function(func1)
var()










def decor_result(result_func):
    def distiction(marks):
        for m in marks:
            if m >=75:
                print("Distiction")
        result_func(marks)
@decor_result

def result(marks):
    for m in marks:
        if m >=33:
            pass
        else:
            print("Fail")
            break
    else:
        print("pass"):
result([50,40,60,80,75])



def outer(x):
    def inner(y):
        return x+y
    return inner

add_five = outer(5)
result = add_five(6)
print(result)


