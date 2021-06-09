with open("file1.txt", "r+")as f:
    f.seek(len(f.read()))
    f.write("woah that was cool")



 