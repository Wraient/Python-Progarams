numbers = [1,2,3,4]
sqaures = list(map((lambda x:x**2), numbers))
print(sqaures)

sqaures_new = [i**2 for i in numbers]
print(sqaures_new)

names = ["abc", "abcd", "abcdef"]
new_func = list(map((lambda x:x+"69"), names))
print(new_func)


