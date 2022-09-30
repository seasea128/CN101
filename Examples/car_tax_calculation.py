#!/usr/bin/env python3

cc = int(input("Enter cc: "))

tax = 0

if cc <= 600:
    tax = cc * 0.5
elif cc <= 1800:
    tax = 300 + ((cc - 600) * 1.4)
else:
    tax = 300 + 1680 + ((cc - 1800) * 3)

print(tax)
