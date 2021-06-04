user = {
    "name" : "Rushikesh",
    "age"  : 16,
    "height" : 69,
}
print(user["name"])
# popped = user.pop("name")
# print(popped)

print(user.get("heights"))
print(user.values())
for i in user:
    print(f" {i} : {user[i]}")

for key, value in user.items():
    print(f" {key} : {value}")



