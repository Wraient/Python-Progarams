l_fruits = ["mango", "grapes", "apple"]
print(sorted(l_fruits))
t_fruits = ("mango", "grapes", "apple")
print(sorted(t_fruits))
s_fruits = {"mango", "grapes", "apple"}
print(sorted(s_fruits))

guitars = [
    {"model" : "yamaha f310", "price":8400},
    {"model" : "faith naptune", "price":50000},
    {"model" : "faith apollo venus", "price":35000},
    {"model" : "taylor 814ce", "price": 450000},
]
print(sorted(guitars, key = lambda d:d["price"], reverse = True))
