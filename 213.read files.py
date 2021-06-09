# readfile
# open function
# read method
# seek method
# tell method
# readline method
# readlines method
# lines method
# close method



f = open(r"/home/kali/Documents/Harshit Vashishta Practice/file1.txt")

# print(f.read())
# print(f.tell())
# f.seek(0)
# print(f.tell())
# print(f.read())

# print(f.readline(), end = "")
# print(f.readline(), end = "")
# print(f.readline(), end = "")
# print(f.readline(), end = "")

# for i in f.readlines()[:2]:
#     print(i, end="")

print(f.name)
print(f.closed)
f.close()
print(f.closed)

