from functools import wraps

def decorator_f(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"You are calling {func.__name__} function")
        print(func.__doc__)
        return func(*args, **kwargs)
    return wrapper

@decorator_f
def cube(a):
    """This function takes 1 argument and returns its cube"""
    return a**2

print(cube(5))



