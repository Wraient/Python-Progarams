def generator(n):
    for i in range(2, n+1,2):
        yield i

for num in generator(10):
    print(num)