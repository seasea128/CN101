#!/usr/bin/env python3

number = int(input("Add number: "))
evenCount = 0
oddCount = 0

while number != -1:
    if number % 2 == 0:
        evenCount += 1
    else:
        oddCount += 1
    number = int(input("Add number: "))

print(f"\nAll numbers = {evenCount + oddCount}")
print(f"Even numbers = {evenCount}")
print(f"Odd numbers = {oddCount}")
