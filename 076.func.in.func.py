def greater(a, b):
    if a > b:
        return a
    return b
    
def greatest(a, b, c):
    return greater(greater(a, b), c)

print(greatest(1, 2, 3))