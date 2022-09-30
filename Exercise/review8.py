#!/usr/bin/env python3

number = int(input("Enter the number:"))

totalSum = 1

for i in range(number, 0, -1):
    totalSum *= i

print(f"{number}! = {totalSum}")
