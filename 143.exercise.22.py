def to_power(num, *args):
    return ["Hey, you didnt pass any args" if args == False else i**num for i in args]

nums = [1,2,3]
print(to_power(3, *nums))


