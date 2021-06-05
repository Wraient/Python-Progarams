dick = {f"Square of {num} is":num**2 for num in range(1,11)}
for k, v in dick.items():
    print(f"{k} {v}")

name = "Rushikesh"
dit = {char:name.count(char) for char in name}
print(dit)
