# Point coordinates are input as four values separated by space
x1, y1, x2, y2 = (int(i) for i in input().split())

# Vertical line
if x1 == x2:
    print('ERROR')
    exit(0)
# Horizontal line
if y2 == y1:
    print(f'y = {x1}')
else:
    # Linear equation is expressed as y = slope * x + intersect
    slope = (y2 - y1) / (x2 - x1)
    intersect = y1 - slope * x1
    print(f'y = {slope}*x {"+" if intersect >= 0 else "-"} {abs(intersect)}')

