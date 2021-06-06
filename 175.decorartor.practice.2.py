from functools import wraps

# def only_int_allowed(function):
#     @wraps(function)
#     def wrapper(*args, **kwargs):
#         types = []
#         for arg in args:
#             types.append(type(arg)==int)
#         if all(types):
#             return function(*args, **kwargs)
#         else:
#             return "Invalid Input"
#     return wrapper

def only_int_allowed(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        if all([type(arg)==int or type(arg)== float for arg in args]):
            return function(*args, **kwargs)
        return "Invalid Argument"
    return wrapper

@only_int_allowed
def add_all(*args):
    total  = 0
    for arg in args:
        total += arg
    return total

print(add_all(1,2,3,4,5))

