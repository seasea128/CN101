#!/usr/bin/env python3

x = float(input("Enter X: "))
y = float(input("Enter Y: "))

quadrant = 0

if x >= 0:
    if y >= 0:
        quadrant = 1
    else:
        quadrant = 4
else:
    if y >= 0:
        quadrant = 2
    else:
        quadrant = 3

# simpler condition check
# if x >= 0 and y >= 0:
#     quadrant = 1
# elif x < 0 and y >= 0:
#     quadrant = 2
# elif x < 0 and y < 0:
#     quadrant = 3
# elif x >= 0 and y < 0:
#     quadrant = 4

print(f"Quadrant: {quadrant}")
