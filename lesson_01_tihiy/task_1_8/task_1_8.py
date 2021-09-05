# Read year
year = int(input('Please input year: '))

# Check if year is leap
is_leap = (year % 4 and year % 100 != 0) or year % 400 == 0

# Print result
print(f'{year} is leap' if is_leap else f'{year} is not leap')
