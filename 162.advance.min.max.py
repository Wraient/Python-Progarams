names = ["Harshit", "Mohit Vashisth", "z", "ab"]

maxu = max(names, key = lambda name : len(name))
print(maxu)


students = {
    "harshit" : {"score":90, "age":24},
    "mohit" : {"score":75, "age":19},
    "rohit" : {"score":76, "age":23}
}

maxu2 = max(students, key = lambda name : students[name]["score"])
print(maxu2)

students2 = [
    {"name":"harshit", "score":69, "age":24},
    {"name":"mohit", "score":70, "age":19},
    {"name":"rohit", "score":60, "age":23}
]

maxu3 = (max(students2, key = lambda item : item.get("score"))["name"])
print(maxu3)
