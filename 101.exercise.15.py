def odd_even(l):
    odd = []
    even = []
    for i in l:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    return [odd, even]

numbers = [69, 64, 96, 87, 90, 56, 61, 21] #list(range(1,11))
print(odd_even(numbers))

