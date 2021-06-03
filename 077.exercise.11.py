def is_palendrome(string):
    return string[::-1] == string

string = input("Enter you word : ")
print(is_palendrome(string))