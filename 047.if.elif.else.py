age = int(input("Enter your age : "))
if age <= 0:
    print("you cannot watch.")
elif age > 0 and age < 11:
    print("Tiket price : Free")
elif age > 11 and age < 60:
    print("Ticket price : 250")
else:
    print("Ticket price : 200")
