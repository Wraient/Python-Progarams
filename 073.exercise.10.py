def bigpp(a, b):
    if a>b:
        return f"{a} is bigger than {b}"
    elif a==b:
        return f"both number are equal."
    return f"{b} is bigger than {a}"

# print(bigpp(56,56))
a = int(input("Enter First number : "))
b = int(input("Enter Second number : "))
print(bigpp(a,b))