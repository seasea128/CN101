#!/usr/bin/env python3

RETAIL_PRICE = 99

quantity = int(input("Enter quantity: "))

price: float = 0

if quantity < 10:
    price = quantity * RETAIL_PRICE
elif quantity < 20:
    price = quantity * RETAIL_PRICE
    price -= price * (10/100)
elif quantity < 50:
    price = quantity * RETAIL_PRICE
    price -= price * (20/100)
elif quantity < 100:
    price = quantity * RETAIL_PRICE
    price -= price * (30/100)
else:
    price = quantity * RETAIL_PRICE
    price -= price * (40/100)

print(price)
