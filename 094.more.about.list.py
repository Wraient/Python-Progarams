numbers = list(range(1, 11))
print(numbers)

poped_num = numbers.pop()
print(poped_num)
print(numbers)

print(f"position of 6 is {numbers.index(6)}")

def negative_list(l):
    negative = []
    for i in l:
        negative.append(-i)
    return negative

print(negative_list(numbers))
print(type(numbers))