# def add(a,b):
#     return a + b

def new_add(*args):
    total = 0
    for num in args:
        total += num
    return total


# print(new_add(1,2,3))

# l = (1,2,3,4)
# print(new_add(*l))

# def func(**kwargs):
#     print(kwargs)
#     print(type(kwargs))

# func(name = "Harshit", age = 24)

def fu2(name, *args, last_name = "unknown", **kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)    

fu2("harshit", 1,2,3,4, last_name = "Vashisht", a=1, b=2)
