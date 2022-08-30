#!/usr/bin/env python3

BASE_HOURS = 40
OT_MULTIPLIER = 1.5

hours = float(input("Enter the number of hours worked: "))
pay_rate = float(input("Enter the hourly pay rate: "))

if hours > BASE_HOURS:
    overtime_hours = hours - BASE_HOURS

    print(f"Overtime hours: {overtime_hours:.1f}")

    overtime_pay = overtime_hours * pay_rate * OT_MULTIPLIER

    print(f"Overtime pay: {overtime_pay:.1f}")

    gross_pay = BASE_HOURS * pay_rate + overtime_pay
else:
    gross_pay = hours * pay_rate

print(f"The gross pay is {gross_pay:.2f}.")
