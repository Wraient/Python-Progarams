fruits = ["Mango", "Orange"]
fruits.insert(1, "Pineapple")
print(fruits)
fruits1 = ["Grapes", "Apple"]
print(fruits1)
# fruits += fruits1
# print(fruits)
fruits.append(fruits1)
print(fruits)
fruits.extend(fruits1)
print(fruits1)