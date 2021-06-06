def decorator_func(any_function):
    def wrapper_func(*args, **kwargs):
        print("this is a wrapper function")
        return any_function(*args, **kwargs)
    return wrapper_func

@decorator_func
def square(a):
    return a**2

print(square(4))



