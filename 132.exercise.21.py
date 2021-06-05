l = [True, False, [1,2,3], 1, 1.0, 3]
output = [str(i) for i in l if type(i)==int or type(i)==float]
print(output)