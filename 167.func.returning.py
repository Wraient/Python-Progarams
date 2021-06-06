def outer_func():
    def inner_func():
        print("Inside inner func")
    return inner_func

var = outer_func()
var()

def outer_func2(msg):
    def inner_func2():
        print(f"Message is {msg}")
    return inner_func2

var2 = outer_func2("Hello world ! ")
var2()

