#!/usr/bin/env python3

number = int(input("Add number: "))
sum = 0
count = 0

while number != -1:
    sum += number
    count += 1
    number = int(input("Add number: "))

avg = sum / count

print(f"The average is {avg:.1f}")
