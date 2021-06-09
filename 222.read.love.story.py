# with open("Love.story.222.txt", "r", encoding="UTF-8") as f:
#     print(f.encoding)
#     data = f.read()
#     print(data)
with open("python.language.wiki.txt", "r") as f:
    data = f.read(100)
    while len(data)>0:
        print(data)
        data = f.read(100)