#!/usr/bin/env python3

PASSING_GRADE = 80

midterm = int(input("Enter midterm exam score: "))
final = int(input("Enter final exam score: "))

total = midterm + final

print(f"Your score is {total}")

if total > PASSING_GRADE:
    print("You passed.")
