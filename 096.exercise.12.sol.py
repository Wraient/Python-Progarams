def sqaure_list(l):
    sqaure = []
    for i in l:
        sqaure.append(i**2)
    return sqaure

numbers = list(range(1,11))
print(sqaure_list(numbers))