n = input("enter a four digit number : ")
# print(int(n[0])+int(n[1])+int(n[2])+int(n[3]))
i = 0
total = 0
while i < len(n):
    total += int(n[i])
    i+=1
print(total)
