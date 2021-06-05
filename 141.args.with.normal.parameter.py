def multipl(num1, *args):
    multipl = 1
    print(num1)
    for i in args:
        multipl *= i
    return multipl

print(multipl(69, 9,3,57,8))


