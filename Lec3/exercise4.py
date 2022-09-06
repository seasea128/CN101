#!/usr/bin/env python3

RETAIL_PRICE = 99

quantity = int(input("Enter quantity: "))

price = 0
discount = 0

if quantity < 10:
    price = quantity * RETAIL_PRICE
elif quantity < 20:
    price = quantity * RETAIL_PRICE
    discount = price * (10 / 100)
elif quantity < 50:
    price = quantity * RETAIL_PRICE
    discount = price * (20 / 100)
elif quantity < 100:
    price = quantity * RETAIL_PRICE
    discount = price * (30 / 100)
else:
    price = quantity * RETAIL_PRICE
    discount = price * (40 / 100)

if discount > 0:
    print(f"The discount is {discount:.2f}")

print(f"The total price is {price - discount:.2f}")
