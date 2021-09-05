# Read triangle sides input
a, b, c = (float(input()) for _ in range(3))

# Check if triangle is valid
if a + b > c and b + c > a and a + c > b: # Triangle is valid
    print('Triangle is valid')

    # Check sides
    if a == b == c:
        print('Triangle is equilateral')
    elif a != b != c:
        print('Triangle is scalene')
    else:
        print('Triangle is isosceles')
else:
    print('Triangle is invalid')
