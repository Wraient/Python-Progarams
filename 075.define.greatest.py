def greatest(a,b,c):
    if a < b > c:
        return b
    elif b < a > c:
        return a
    else:
        return c

print(greatest(1,2,3))