import time
from functools import wraps

def time_cal(any_func):
    @wraps(any_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        output = any_func(*args,**kwargs)
        t2 = time.time()
        print(f"This function took {round(t2-t1, 2)} seconds to run this code")
        return output
    return wrapper

@time_cal
def test(a):
    for i in range(1,100000):
        print(f"This is line {i}")
    total = a**10
    return total

print(test(5))




