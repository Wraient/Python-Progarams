# if statement
name = "Rushikesh"
if name == "Rushikesh" or name == "rushikesh":
    print(f"You are {name}")
elif name == "Someone" and name == "This":
    print("Fuck off")
else:
    print(f"You ain't {name}")

# while statement
i = 1
while i<11:
    print(f"Fuck you {i}")
    i += 1
# for statement
for i in range(0, 11):
    print(f"Fuck you {i}")

# True and break
while i > 9:
    if i == 10:
        print("bye bitches")
    break

# continue
while i < 15:
    if i == 10:
        pass
    print(i)
    i+=1

for i in "Rushikesh":
    print(i)