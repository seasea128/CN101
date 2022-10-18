#!/usr/bin/env python3

import random

MONEY = 100


def guess(bet, guess):
    actual_value = random.randint(1, 2)
    print(f"The random result is {actual_value}", end="")
    if guess == actual_value:
        print(", you win!")
        print(f"You get {bet} baht")
        return bet
    else:
        print(", you lose!")
        print(f"You lose {bet} baht")
        return -bet


while "y" == input(f"You have {MONEY} baht. Do you want to continue? (y/n) "):
    bet = int(input("Please enter the bet: "))
    guessed = int(input("Please make a guess (1-2): "))
    MONEY += guess(bet, guessed)
