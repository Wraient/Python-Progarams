numbers1 = [2,4,6,8,10]
numbers2 = [1,3,5,7,9,6]

# is_even = lambda l : l if all(l)%2==0 else [x for x in l if x%2==0] 

# print(is_even(numbers2))

even = all(num%2==0 for num in numbers1)
print(even)

odd = any(num%2 ==0 for num in numbers2)
print(odd)

