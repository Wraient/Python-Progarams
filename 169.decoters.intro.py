def decorator_func(func):
    def wrapper_func():
        print("This is a decorator line.")
        func()
    return wrapper_func

@decorator_func
def func1():
    print("this is func 1")

func1()

@decorator_func
def func2():
    print("this is func 2")

func2()

