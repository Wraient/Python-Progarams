def func(*args, reverse_str = False):
    if reverse_str == True:
        return [name[::-1].title() for name in args]
    else:
        return [name.title() for name in args]

print(func(*["rushIKeSh", "HArsHIt"]))

