# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль
# (за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего
# и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

companies_dict = {}

number_of_companies = int(input('Please input number of entries: '))

for _ in range(number_of_companies):
    raw_input = input('Please input company name and quarterly incomes (name q1 q2 q3 q4): ').split()
    companies_dict[raw_input[0]] = sum(float(x) for x in raw_input[1:])

average_income = sum(companies_dict.values()) / len(companies_dict)

print('Companies with income above average:')
for name, income in companies_dict.items():
    if income >= average_income:
        print(f'\t{name}')

print('#' * 80)

print('Companies with income below average:')
for name, income in companies_dict.items():
    if income < average_income:
        print(f'\t{name}')
