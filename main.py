import random

print('Hello Stranger. What is your name')
name = input()

print('Well ' + name + ', I am thinking of a number between 1 and 50 can you guess it ?')
secretNumber = random.randint(1, 50)

for guessesTaken in range(1, 5):
    print('Take a guess.')
    guess = int(input())

    if guess > secretNumber:
        print('Your guess is too High.')
    elif guess < secretNumber:
        print('Your guess is too Low')
    else:
        break
if guess == secretNumber:
    print('Good Job ' + name + ' ! You guessed the number i was thinking in ' + str(guessesTaken) + ' guess, nice work')
else:
    print('Nope, the number i was thinking of was ' + str(secretNumber) + ' try again sometime!')
