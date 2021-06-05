def func(**kwargs):
    for k, v in kwargs.items():
        print(f"{k} : {v}")



func(name = "Harshit", age = 69)

l = {
    "name" : "Harshit",
    "age" : 69,
}

func(**l)





