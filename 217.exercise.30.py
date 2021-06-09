with open("exercise.1.txt") as rf:
    with open("output.txt", "a") as wf:
        for i in rf.readlines():
            name, salary = i.split(",")
            wf.write(f"{name}'s salary is {salary}")

