l1 = [1,3,5,7]
l2 = [2,4,6,8]

# l = [(1,2),(3,4),(5,6),(7,8)]
# ziped = zip(*l)
new_l = []

for i in zip(l1,l2):
    new_l.append(max(i))

print(new_l)

# l1, l2 = list(zip(*l))
# print(f"{list(l1)}\n{list(l2)}")



