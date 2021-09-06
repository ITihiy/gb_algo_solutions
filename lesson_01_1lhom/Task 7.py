# 7. По длинам трех отрезков, введенных пользователем, определить возможность существования
# треугольника, составленного из этих отрезков. Если такой треугольник существует, то
# определить, является ли он разносторонним, равнобедренным или равносторонним.

print('Enter dimensions of triangle: ')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if a + b > c and a + c > b and b + c > a:
    print('Triangle is valid!')
    if a == b and b == c and c == a:
        print('Equilateral triangle ')
    elif (a == b and b != c) or (b == c and c != a) or (c == a and a != b) :
        print('Isosceles triangle')
    else:
        print('Versatile triangle')
else:
    print('This is not triangle!')
