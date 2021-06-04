user = {}
# name = input("Name : ")
user["name"] = input("name : ")
user["age"] = input("age : ")
user["fav_movies"] = input("Fav Movies : ").split(", ")
user["fav_songs"] = input("Fav songs : ").split(", ")

for key, value in user.items():
    print(f"{key} : {value}")