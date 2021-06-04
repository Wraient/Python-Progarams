def fucn(num1, num2):
    add = num1 + num2
    multipl = num1*num2
    return add, multipl

print(type(fucn(34, 35)))

add, multipl = fucn(34, 35)
print(add)
print(type(add))
print(multipl)
print(type(multipl))
