def generator(n):
    for i in range(n+1):
        if i%2==0:
            yield i

evens = generator(10)
for i in evens:
    print(i)



