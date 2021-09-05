a = 5
b = 6

# AND
# 5 = 101
# 6 = 110
#
# 101 &
# 110
# 100 = 4

print(a & b)


# OR
# 5 = 101
# 6 = 110
#
# 101 |
# 110
# 111 = 7

print(a | b)

# XOR
# 5 = 101
# 6 = 110
#
# 101 ^
# 110
# 011 = 3

print(a ^ b)

# LEFT SHIFT
# 101 >> 2:
# 1. 010
# 2. 001
# result = 1

print(a >> 2)

# RIGHT SHIFT
# 101 << 2:
# 1. 1010
# 2. 10100
# result = 20 or (5 * 4)

print(a << 2)
