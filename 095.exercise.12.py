def sqaure_list(l):
    sqaures = []
    for i in l:
        sqaures.append(i**2)
    return sqaures

numbers = [1, 2, 3, 4, 5]
print(sqaure_list(numbers))