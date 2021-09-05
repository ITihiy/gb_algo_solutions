letter_number = int(input('Please input a letter number: '))


# Check if input is correct
if not 0 < letter_number < 27:
    print('Invalid input')
    exit(-1)

print(f'Letter is "{chr(letter_number + ord("a") - 1)}"')
