#!/usr/bin/env python3

MARK_UP = 2.5
another = "y"

while another == "y" or another == "Y":
    wholesale = float(input("Enter the item's wholesale cost: "))

    while wholesale < 0:
        print("ERROR: The cost cannot be negative")
        wholesale = float(input("Enter the item's wholesale cost: "))

    retail = wholesale * MARK_UP

    print(f"Retail price: {retail:.2f}")

    another = input("Do you have another item? (Enter y for yes): ")
