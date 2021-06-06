def to_power(n):
    def cal_power(x):
        print(x**n)
    return cal_power

cube = to_power(3)
cube(2)





