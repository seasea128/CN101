#!/usr/bin/env python3

price = int(input("Price: "))
while price > 1000:
    print("Price must be less than 1000 baht")
    price = int(input("Price: "))

amount_paid = int(input("Amount paid: "))
while amount_paid < price or amount_paid > 1000:
    print("Amount paid must be higher than price and less than 1000 baht")
    amount_paid = int(input("Amount paid: "))

change = amount_paid - price
print(f"Change: {change}")
five_hundred = change // 500
if five_hundred > 0:
    print(f"{five_hundred} 500-Baht bill (s)", end=",")
one_hundred = change % 500 // 100
if one_hundred > 0:
    print(f"{one_hundred} 100-Baht bill (s)", end=",")
fifty = change % 100 // 50
if fifty > 0:
    print(f"{fifty} 50-Baht bill (s)", end=",")
twenty = change % 50 // 20
if twenty > 0:
    print(f"{twenty} 20-Baht bill (s)", end=",")
ten = change % 50 % 20 // 10
if ten > 0:
    print(f"{ten} 10-Baht coin (s)", end=",")
five = change % 10 // 5
if five > 0:
    print(f"{five} 5-Baht coin (s)", end=",")
one = change % 5
if one > 0:
    print(f"{one} 1-Baht coin (s)", end=",")

print("\n")
