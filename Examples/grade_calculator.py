#!/usr/bin/env python3

MAX_POINTS = 50

num_students = int(input("Enter number of students: "))
num_exams = 2

for student in range(num_students):
    total = 0
    print(f"Student {student + 1}")
    for exam in range(num_exams):
        score = float(input(f"Enter score for exam {exam + 1}: "))
        while score < 0 or score > MAX_POINTS:
            print("Invalid Input")
            score = float(input(f"Enter score for exam {exam + 1}: "))
        total += score

    average = total / num_exams
    print(f"Average score: {average:.2f}")
    if total >= 80:
        print("A")
    elif total >= 70:
        print("B")
    elif total >= 60:
        print("C")
    elif total >= 50:
        print("D")
    else:
        print("F")
