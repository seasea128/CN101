#!/usr/bin/env python3


def print_text():
    print("This program will find an average of 2 numbers.")
    print("The program will then print the resulting average value.")


def get_average():
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    return (x + y) / 2


def main():
    print_text()
    average = get_average()
    print(f"The average is => {average:.2f}")


main()
