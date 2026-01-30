print('Welcome to the Quiz Game!')
play = str(input("Lets go play the game? [yes/no] ")).strip().lower()
correct = 0 
incorrect = 0

while play != 'yes' and play != 'no':
    play = str(input("Lets go play the game? [yes/no] ")).strip().lower()
    
if play.strip().lower() == 'yes':
    print("What does 'CPU' mean? ")
    answer = str(input('')).strip().lower()
    if answer == 'central processing unit':
        correct += 1
        print('You are correct!')
    else:
        incorrect += 1
        print('You are incorrect!')
else:
    quit()

print(f"total correct answers: {correct}\n total errors: {incorrect}")