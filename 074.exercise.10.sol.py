def greater(a, b):
    if a>b:
        return a
    else:
        return b

num1 = int(input("Enter First number : "))
num2 = int(input("Enter Second number : "))
bigger = greater(num1, num2)

print(f"{bigger} is greater")