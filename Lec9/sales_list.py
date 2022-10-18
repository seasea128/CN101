#!/usr/bin/env python3


def main():
    NUM_DAYS = int(input("Enter the number of days: "))

    sales = [0] * NUM_DAYS

    print("Enter the sales for each days.")

    for i in range(0, len(sales)):
        sales[i] = int(input(f"Day #{i+1}: "))

    print("List after the end of period: ")
    print(sales)

    print(f"The total values is {sum(sales)}")
    print(f"The maximum value is {max(sales)}")
    print(f"The minimum value is {min(sales)}")
    print(f"The average value is {sum(sales)/len(sales):.2f}")


main()
