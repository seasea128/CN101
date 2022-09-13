#!/usr/bin/env python3

TARGET = float(input("Enter the target saving: "))
days = 0
saving = 0

while saving < TARGET:
    days += 1
    deposit = float(input("Please enter your daily deposit: "))
    saving += deposit

    if saving > TARGET:
        break

    print(f"Current saving: {saving}")
    print(f"Saving left until target: {TARGET - saving}")
    print(f"Days passed since first saving: {days}")
    print(f"Days left until target: {(TARGET - saving) / (saving / days):.2f}")

print(f"The total saving that you save is {saving}")
print(f"The average saving per day is {saving / days:.2f}")
