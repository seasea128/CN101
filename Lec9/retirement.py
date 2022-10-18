#!/usr/bin/env python3

CONTRIBUTION_RATE = 0.05


def main():
    gross_pay = float(input("Enter the gross pay: "))
    bonus = float(input("Enter the amount of bonuses: "))
    show_pay_contrib(gross_pay)
    show_bonus_contrib(bonus)


def show_pay_contrib(gross):
    contrib = gross * CONTRIBUTION_RATE
    print(f"Contribution for gross pay: ${contrib:.2f}")


def show_bonus_contrib(bonus):
    contrib = bonus * CONTRIBUTION_RATE
    print(f"Contribution for bonuses: ${contrib:.2f}")


main()
