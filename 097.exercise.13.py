numbers = list(range(1,11))

def reverse_list(l):
    reversed = []
    i = 1
    while i <= len(l):
        reversed.append(l[-i])
        i += 1
    return reversed

# def reverse_list(l):
#     reversed = []
#     for i in range(0,len(l)):
#         reversed.append(l.pop())
#     return reversed

print(reverse_list(["word1", "word2"]))

print(reverse_list(numbers))
