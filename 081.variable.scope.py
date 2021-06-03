x = 69 # global variable
def add(num):
    global x
    x = -69
    num -= num + 69
    return num

def sub(num):
    num += 69
    return num

num = int(input("Enter the num : "))
print(x)
print(add(num))
print(x)