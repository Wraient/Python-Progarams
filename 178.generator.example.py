def nums(n):
    for i in range(1,n+1):
        yield i

number = nums(10)

for i in number:
    print(i)

for i in number:
    print(i)

