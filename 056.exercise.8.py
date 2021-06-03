name = input("Enter your name : ")
letter = ""
i = 0
while name[i] not in letter:
    if i<len(name):
        print(f"{name[i]} : {name.count(name[i])}")
        letter += name[i]
        i += 1
# while i<len(name):
#     if lowercase[i] in letter:
#         pass
#     elif lowercase[i] not in letter:
#         print(f"{name[i]} : {lowercase.count(lowercase[i])}")
#         letter += lowercase[i]
#         i += 1
