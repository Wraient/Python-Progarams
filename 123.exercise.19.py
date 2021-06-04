users = {}
# name = input("Name : ")
users["name"] = input("name : ")

users["age"] = input("age : ")

users["fav_movies"] = list(input("Fav Movies : ").split(", "))

users["fav_songs"] = list(input("Fav songs : ").split(", "))


for i in users:
    print(f"{i} : {users[i]}")


