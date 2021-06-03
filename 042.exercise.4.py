import random
winning_number = random.randint(0, 100)
guess_count = 3
guess = 1
user_input = int(input("guess a number : "))
if guess_count > guess:
    if user_input == winning_number:
        guess = 5
        print("YOU WINN!!!")
else:
    if user_input > winning_number:
        print("Too High")
        guess+=1
        print(winning_number)
    elif user_input < winning_number:
        print("Too Low")
        print(winning_number)
        guess+=1