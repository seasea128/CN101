#!/usr/bin/env python3

int1 = int(input("Enter integer #1: "))
int2 = int(input("Enter integer #2: "))
int3 = int(input("Enter integer #3: "))

maxVal = 0

if int1 > int2 and int1 > int3:
    maxVal = int1
elif int2 > int1 and int2 > int3:
    maxVal = int2
elif int3 > int1 and int3 > int2:
    maxVal = int3
else:
    print("Something is wrong")

print(f"The maximum number is {maxVal}")

# Another, simpler impl

# intArr = [int1, int2, int3]
# print(f"The maximum number is {max(intArr)}")
