# def is_palindrom(word):
#     reversed_string = word[::-1]
#     if word == reversed_string:
#         return True
#     else:
#         return False

# def is_palindrom(word):
#     reversed_string = word[::-1]
#     if word == reversed_string:
#         return True
#     return False

# def is_palindrom(word):
#     reversed_string = word[::-1]
#     return word == reversed_string

def is_palindrom(word):
    return word == word[::-1]

print(is_palindrom("naman"))
print(is_palindrom("horse"))
