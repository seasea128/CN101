#!/usr/bin/env python3

gender = input("Enter gender: ")
age = int(input("Enter age: "))

if gender == "male":
    if age > 18:
        print("Man")
    else:
        print("Boy")
elif gender == "female":
    if age > 18:
        print("Woman")
    else:
        print("Girl")
