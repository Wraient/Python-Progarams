while True:
    try:
        age = int(input("Enter your age: "))
        break
    except ValueError:
        print("You didn\'t enter a number..")
    except:
        print("Unexpected error...")
    else:
        print(f"You won")
        break
    finally:
        print("Finally block...")

if age>18:
    print("You can play this game")
else:
    print("You can\'t play this game")

