from functools import wraps
def decorator_func(any_function):
    @wraps(any_function)
    def wrapper_func(*args, **kwargs):
        """this is wrapper function's doc string"""
        print("this is a wrapper function")
        return any_function(*args, **kwargs)
    return wrapper_func

@decorator_func
def square(a):
    """This function takes a numer and returns its square"""
    return a**2

print(square.__name__)
print(square.__doc__)



