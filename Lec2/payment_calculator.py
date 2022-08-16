#!/usr/bin/env python3

total_amount = int(input("Enter the total amount (Baht): "))
input_bills_amount = int(input("Enter the bills (thousands): "))

change = (input_bills_amount * 1000) - total_amount
print(f"The change is {change} baht")

five_hundreds_amount = change // 500
print(f"{five_hundreds_amount} of 500-baht bills")
change -= five_hundreds_amount * 500

hundreds_amount = change // 100
print(f"{hundreds_amount} of 100-baht bills")
change -= hundreds_amount * 100

fifty_amount = change // 50
print(f"{fifty_amount} of 50-baht bills")
change -= fifty_amount * 50

twenty_amount = change // 20
print(f"{twenty_amount} of 20-baht bills")
change -= twenty_amount * 20

ten_amount = change // 10
print(f"{ten_amount} of 10-baht coins")
change -= ten_amount * 10

five_amount = change // 5
print(f"{five_amount} of 5-baht coins")
change -= five_amount * 5

one_amount = change
print(f"{one_amount} of 1-baht coins")
