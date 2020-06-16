import random
print("What is your name ")
name = input()
if name == input():
    print("Welcome", name)
operation = input('''
What do you want to do: 
1 for play a game
2 for exit
''')

if operation == '2':
    print("See you Later")
    exit()
if operation == '1':
    print("Let play a game")

guessesTaken = 0

print('Hello what is your name? ')
myName = input()

number = random.randint(1, 20)
print('Well', myName, 'i am thinking of a number between 1 and 20.')

while guessesTaken < 6:
    print('Take a guess.')
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:

     print('Your number is too low.')

    if guess > number:
        print('Your guess is to high.')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job, '+ myName + '! You guessed my number in ' + guessesTaken + ' guesses!')

    if guess != number:
        print('You are wrong. The number I was thinking of was ' + number)
