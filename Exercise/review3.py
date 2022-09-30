#!/usr/bin/env python3

input1 = int(input("Input 1: "))
input2 = int(input("Input 2: "))
input3 = int(input("Input 3: "))
input4 = int(input("Input 4: "))
input5 = int(input("Input 5: "))

inputArr = [input1, input2, input3, input4, input5]

matches = 0

for i in inputArr:
    if i == 8 or i == 12 or i == 20 or i == 55 or i == 61:
        matches += 1

if matches >= 3:
    print("You wins!")
else:
    print("You lose")
