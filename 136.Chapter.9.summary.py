square = [i**2 for i in range(1,11)]
print(square)

even_num = [i for i in range(1,11) if i%2==0]
print(even_num)

racist_num = [i*2 if(i%2==0) else -i for i in range(1,11)]
print(racist_num)

nested_l = [[i for i in range(1,4)] for j in range(3)]
print(nested_l)

