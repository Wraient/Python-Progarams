import random
winning_number = random.randint(0, 100)
guess_count = 0
guess = input("Enter your guess : ")
while True:
    guess_count += 1
    if int(guess)>winning_number:
        print("Too High")
    elif int(guess)==winning_number:
        print(f"Congratulations! You Won, Guess Count : {guess_count}")
        break
    else:
        print("Too Low")
    guess = input("Guess again : ")
