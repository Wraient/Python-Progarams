def add(a,b):
    if type(a) == int and type(b) == int:
        return a + b
    raise TypeError("Wrong data type")


print(add("5","6"))