# def reverse_list(l):
#     l.reverse()
#     return l

# def reverse_list(l):
#     return l[::-1]


def reverse_list(l):
    reversed = []
    for i in range(0,len(l)):
        reversed.append(l.pop())
    return reversed

numbers = list(range(1,11))
print(reverse_list(numbers))