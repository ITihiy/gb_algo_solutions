first_letter = input('Please input a letter: ')
second_letter = input('Please input another letter: ')

# Check if input is correct
if (not ('a' <= first_letter <= 'z')) or (not ('a' <= second_letter <= 'z')):
    print('Invalid input')
    exit(-1)

print(f'First letter number is {ord(first_letter) - ord("a") + 1}')
print(f'Second letter number is {ord(second_letter) - ord("a") + 1}')
print(f'Distance between letters is {abs(ord(first_letter) - ord(second_letter))}')
