import random

print('Welcome to the Game!')
randomNumber = random.randint(0, 10)
trueOrFalse = True
attempts = 0

guess = int

while guess != randomNumber:
    try:
        guess = int(input("Guessing the number: "))
        attempts += 1
        if guess > randomNumber:
            print('Lower')
        elif guess == randomNumber:
            print("CORRECT!")
            print(f'Numero de tentativas: {attempts}')
        else:
            print('Higher')
    except:
        print('Digite um numero válido')