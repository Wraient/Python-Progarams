def wordcounter(s):
    count = {}
    for i in s:
        count[i] = s.count(i)
    return count


print(wordcounter("harshit"))