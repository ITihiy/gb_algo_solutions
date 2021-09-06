from random import randint

number_to_guess = randint(0, 100)
tries = 10

print('#' * 80)
print('GUESS A NUMBER')
print('#' * 80, '\n')

while tries:
    tries -= 1
    current_guess = int(input('Please enter your guess (0 to 100): '))
    if current_guess == number_to_guess:
        print(f'\nYou guess is correct! Number was {number_to_guess}')
        break
    elif current_guess < number_to_guess:
        print(f'Your guess {current_guess} is too low. Try again ({tries} tries left). ')
    else:
        print(f'Your guess {current_guess} is too high. Try again ({tries} tries left). ')
else:
    print(f'\nSorry. You lost. Correct number was {number_to_guess}')
