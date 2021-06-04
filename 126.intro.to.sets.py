s = {1,2,3,3,4,5,6,7,8,9,10}
print(s)

l = [1,1,1,1,1,1,2,23,6,7,8,9,9,9,10]
print(l)
l = list(set(l))
print(l)

s = {1,1.0,2.3,3,4.0,"string"}
print(s)
s.add("another string")
print(s)
s.discard("string")
print(s)
s.discard("stringsidsa")
print(s)
