#!/usr/bin/env python3

input = int(input("Enter an integer number:"))

count = 0

for i in range(1, input + 1):  # range will not include the stop args
    if input % i == 0:
        count += 1

if count > 2:
    print(f"{input} is not a prime number.")
else:
    print(f"{input} is a prime number.")
