import random

computer_wins = 0
user_wins = 0
draw = 0

options = ['rock', 'paper', 'scissors']

while True:
    user_opt = str(input("Rock, Paper, Scissors or Q for quit: ")).strip().lower()

    if user_opt == 'q':
        break
    if user_opt not in options:
        continue

    random_number = random.randint(0, 2)
    random_opt = options[random_number]

    if user_opt == random_opt:
        draw += 1
        print(f'The computer played {random_opt} || Draw.')
    elif user_opt == 'rock' and random_opt == 'scissors' or user_opt == 'paper' and random_opt == 'rock' or user_opt == 'scissors' and random_opt == 'paper':
        user_wins += 1
        print(f'The computer played {random_opt} || You won.')
    else:
        computer_wins += 1
        print(f'The computer played {random_opt} || You lost.')

print(f"User wins: {user_wins}\nComputer wins: {computer_wins}\nDraws: {draw}")