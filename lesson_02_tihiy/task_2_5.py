START_SYMBOL = 32
END_SYMBOL = 127

for index, char in enumerate(range(START_SYMBOL, END_SYMBOL + 1)):
    if index > 0 and index % 10 == 0:
        print()
    print(f'{char}: {chr(char)}', end='\t')
