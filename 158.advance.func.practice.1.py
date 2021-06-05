# def average(*args):
#     average = 0
#     for i in range(len(args)):
#         for j in args:
#             args[i]+ 

# def average_find(*args):
#     average = []
#     for i in zip(*args):
#         average.append(round(sum(i)/len(args), 2))
#     return average

# print(average_find([1,3,5],[1,4,6],[1,2,3]))


average_finder = lambda *args : [round(sum(i)/len(args), 2) for i in zip(*args)]

print(average_finder([1,3,5],[1,4,6]))

