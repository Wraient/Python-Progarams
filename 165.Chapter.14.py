def sqaure(a):
    return a**2

s = sqaure


print(s.__name__)
print(sqaure.__name__)
print(s)
print(sqaure)
print(s is sqaure)
print(s(7))