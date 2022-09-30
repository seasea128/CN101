#!/usr/bin/env python3

import math

width = float(input("Enter the width of rectangle: "))
height = float(input("Enter the height of rectangle: "))

r = 0

if width < height:
    r = width / 2
else:
    r = height / 2

area = math.pi * (r**2)

print(f"\nThe radius of the biggest circle in this rectangle is {r:.1f}")
print(f"The area of the circle is {area:.2f}")
