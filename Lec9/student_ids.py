#!/usr/bin/env python3


def main():
    student_ids = []
    x = int(input("Add student to the list (Enter 0 to finish): "))
    while x > 0:
        if x in student_ids:
            print(f"Student already exist at {student_ids.index(x)}")
        else:
            student_ids.append(x)
        x = int(input("Add student to the list (Enter 0 to finish): "))

    print(student_ids)


main()
