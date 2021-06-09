with open("219.exercise.31.html", "r") as webpage:
    with open("output.3.221.txt", "a") as wf:
        link_exist = True
        page = webpage.read()
        while link_exist:
            pos = page.find("<a href=")
            if page.find("<a href=") == -1:
                link_exist = False
            else:
                first_quote = page.find("\"", pos + 1)
                second_quote = page.find("\"", first_quote+1)
                url = page[first_quote+1:second_quote]
                wf.write(url + '\n')
                page = page[second_quote+1:]