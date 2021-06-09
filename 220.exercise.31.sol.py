with open("219.exercise.31.html","r") as webpage:
    with open("Output.exercise.31.txt","a") as wf:
        for line in webpage.readlines():
            if "<a href=" in line:
                pos = line.find("<a href=")
                first_quote = line.find("\"", pos+1)
                second_quote = line.find("\"", first_quote+1)
                url = line[first_quote+1:second_quote]
                wf.write(url + "\n")

