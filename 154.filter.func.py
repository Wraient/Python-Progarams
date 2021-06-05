numbers = [2,3,1,3,4,5,7,9,4,7,8,4]
even = filter(lambda x:x%2==0, numbers)
print(even)
for i in even:
    print(i)


