with open("file1.txt", "r+") as rf:
    with open("file2.txt", "r+") as wf:
        wf.write(rf.read())

