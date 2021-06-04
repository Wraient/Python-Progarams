mixed = (1,2,3,4.0)
print(type(mixed))
for i in mixed:
    print(i)

x = (1)
print(type(x))

tupel_with_one_variable = (1,)
print(type(tupel_with_one_variable))

bikes = "Yamaha", "Honda", "Suzuki", "Maruti"
print(type(bikes))
print(bikes)

biker1, biker2, biker3, biker4 = (bikes)
print(biker1, biker2)
print(type(biker1))

print(bikes)

mixed_tuple = ("Attack on titan", "Death Note", ["Lucifer", "Money Heist", "Thor"])
print(mixed_tuple)
popped = mixed_tuple[2].pop()
print(popped)
print(mixed_tuple)

mixed_tuple[2].append("Mirzapur")
print(mixed_tuple)

print(min(mixed))
print(max(mixed))
