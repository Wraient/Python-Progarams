name, ammount = input("Enter Your name and ammount of stars : ").split(",")
name = name.replace(" ", "")
ammount = int(ammount.replace(" ", ""))
print(name.center(len(name)+ammount, "*"))