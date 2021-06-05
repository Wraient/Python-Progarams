def multipl(*args):
    multipl = 1
    for i in args:
        multipl *= i
    return multipl

nums = [1,2,3]
print(multipl(*nums))
