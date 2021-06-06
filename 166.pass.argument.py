my_map = lambda func, l : [func(i) for i in l]
# square = lambda a : a**2
print(my_map(lambda a : a**2, [1,2,3,4,5,6,7]))


