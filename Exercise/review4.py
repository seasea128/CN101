#!/usr/bin/env python3

saleAmount = int(input("Enter a sale amount: "))

rate = 0

if saleAmount <= 5000:
    rate = 5
elif saleAmount <= 30000:
    rate = 10
else:
    rate = 15

discount = (saleAmount * rate) / 100

print(f"Discount = {discount:.2f}")
print(f"You pay only {saleAmount - discount:.2f}")
