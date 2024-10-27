### Part Two -- your code goes here. 

import random 
number = random.randint(1,100)
print('Pick a number between 1 and 100?')
guess = 0
while guess != number:
    guess = int(input('Enter your number?'))

    if guess < number:
        print('Too low')
    elif guess > number:
        print('Too high')

    else:
        print('Correct Number!')

