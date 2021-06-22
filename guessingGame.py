import random

print('Welcome To The Number Guessing Game!')

number = random.randint(1,9)

chances = 0

print('Guess a number between the numbers 1 - 9')

while chances < 5:
    guess = int(input('Enter your guess here: '))

    if guess == number:  
        print('Congrats! You won!')
        break
    elif guess < number:
        print('Your guess is too low. Guess a number higher than ', guess)
    else:
        print('Your guess was too high. Guess a number lower than ', guess)
    
    chances += 1

if chances == 5:
    print('You lose! The number was', number)