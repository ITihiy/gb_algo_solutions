# 3.По введенным пользователем координатам двух точек вывести уравнение прямой вида
# y = kx + b, проходящей через эти точки.

print("Enter coordinate numbers: ")
x1 = float(input("x1 = "))
y1 = float(input("y1 = "))
x2 = float(input("x2 = "))
y2 = float(input("y2 = "))

print("Equation of a straight line passing through these points:")
k = (y1 - y2) / (x1 - x2)
b = y2 - k * x2
print(f" y = {k}*x + {b}")
