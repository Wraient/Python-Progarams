name, age = input("Enter your name and your age : ").split()
if name.lower()[0]=="a" and int(age)>10:
    print("You can watch this movie.")
else:
    print("You can't watch this movie.")
