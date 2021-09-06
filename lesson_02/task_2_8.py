seq_prompt = 'Please enter sequence of numbers: '
number_prompt = 'Please enter number to count: '
print([int(x) for x in input(seq_prompt).split()].count(int(input(number_prompt))))
