#!/usr/bin/env python3

amount = float(input("Enter full amount: "))
service_charge = float(input("Enter service charge: "))
tax_rate = float(input("Enter tax rate: "))

service = amount * (service_charge / 100)
amount_with_service = amount + service
tax = amount_with_service * (tax_rate / 100)
amount_with_tax = amount_with_service + tax

print("The total amount to pay:")
print(f"Without tax {amount:28.2f}")
print(f"Service charge {service_charge:.2f}% {tax:18.2f}")
print(f"With service charge {amount_with_service:20.2f}")
print(f"Tax {tax_rate:.2f}% {tax:29.2f}")
print(f"With tax {amount_with_tax:31.2f}")
