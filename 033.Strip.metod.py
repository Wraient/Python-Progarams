name = "     Rush       ikesh      "
dots = "|||||||||||||||||||||"

print(name + dots)
print(name.lstrip()+dots)
print(name.rstrip()+dots)
print(name.strip()+dots)
print(name.replace(" ", ""))

name, char = input("enter comma seperated name and character : ").split(",")
name = name.replace(" ", "")
char = char.replace(" ", "")
print(f"length of your name is : {len(name)}")
print(f"character count : {name.lower().count(char.lower())}")