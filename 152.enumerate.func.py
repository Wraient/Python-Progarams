names = ["abc", "def", "Harshit"]

def pos_finder(l, s):
    for pos, name in enumerate(l):
        if name == s:
            return pos
    return -1

# pos_finder = lambda l,s : pos if name == s else "-1" for pos, name in enumerate(l)

print(pos_finder(names,"def"))

