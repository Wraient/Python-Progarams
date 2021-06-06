def my_sum(*args):
    if all([(type(i)==int or type(i)==float) for i in args]):
        total = 0
        for i in args:
            total += i
        return total
    return "FUCK OFF"


num = [1,2,3,4,5,6,7,8,9,10,11]
print(my_sum(*num))

