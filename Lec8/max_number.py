#!/usr/bin/env python3


def maxi(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c


x = int(input("Enter integer #1: "))
y = int(input("Enter integer #2: "))
z = int(input("Enter integer #3: "))
maximum = maxi(x, y, z)
print(f"The maximum number is {maximum}")

# Another, simpler impl

# intArr = [int1, int2, int3]
# print(f"The maximum number is {max(intArr)}")
