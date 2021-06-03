def reverse_str(l):
    reversed = []
    for i in l:
        reversed.append(i[::-1])
    return reversed

words = ["abc", "tuv", "xyz"]
print(reverse_str(words))
