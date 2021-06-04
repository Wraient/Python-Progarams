user_info = {
    "Name" : "Rushikesh",
    "Age" : 18,
    "Fav_movie" : ["Robot", "Social Networks", "Twitter"],
    "Fav_tunes" : ["Tokyo Ghoul", "Weathering with you"]
}

# Add
user_info["fav_songs"] = ["song1", "song2"]
print(user_info)

print("\n")

# delete
user_info.pop("Fav_tunes")
print(user_info)

print("\n")

# random delete
popped = user_info.popitem()
print(f"popped item is {popped}")
print(user_info)

