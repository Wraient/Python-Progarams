from csv import reader

with open("file.csv", "r") as f:
    file = reader(f) # iterator
    next(file)
    for i,j,k in file:
        print(f"Name : {i}, Email : {j}, Phone : {k}")