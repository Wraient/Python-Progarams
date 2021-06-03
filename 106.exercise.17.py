def how_many(l):
    total = 0
    for i in l:
        if type(i) ==  list:
            total += 1
        continue
    return total

numbers = [1,2,3,[1,2],[3,4]]
print(how_many(numbers))
