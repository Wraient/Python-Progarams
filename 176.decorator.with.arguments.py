from functools import wraps

def only_allow(data_type):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if all([type(arg)==data_type for arg in args]):
                return func(*args, **kwargs)
            return "Invalid Input"
        return wrapper
    return decorator


@only_allow(str)
def string_add(*args):
    string = ""
    for i in args:
        string += i
    return string

print(string_add("Harshit ", "Vashist", "a"))

