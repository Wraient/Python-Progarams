mixed = [1, 2, 3, ["four", "five", "6"], 6.9, True, False, None]
print(mixed[3])
print(mixed[5])
print(mixed[6])
print(mixed[7])
print(mixed[8])
print(mixed[9])
mixed[1]="two"
print(mixed)
mixed[1:]="two"
print(mixed)
mixed[1:]=["two", "three", "four", 5, None]
print(mixed)