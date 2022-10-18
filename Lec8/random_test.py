#!/usr/bin/env python3

import random


def main():
    while "y" == input("Do you want to continue? (y/n) "):
        x = int(input("Please make a guess (1-6) : "))
        r = random.randint(1, 6)
        print(f"The random value is {r}")
        if x == r:
            print("You win")
        else:
            print("You lose")


main()
