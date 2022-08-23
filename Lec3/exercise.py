#!/usr/bin/env python3

midterm = int(input("Enter midterm exam score: "))
final = int(input("Enter final exam score: "))

total = midterm + final

print(f"Your score is {total}")

if total > 80:
    print("You passed.")
