#!/usr/bin/env python3

choice = 10


def printMes():
    print("1. asdfh")
    print("2. asdfh")


list_test = [
    ["test", "test", "test"],
]


def editUser():
    pos = int(input("Index: "))
    if pos >= len(list_test):
        print("Index out of bound")
        return
    var = int(input("Variable to edit: "))
    if var >= len(list_test[pos]):
        print("Index out of bound")
        return
    val = input("Value: ")
    list_test[pos][var] = val
    print(list_test)


# while choice != 0:
#    choice = int(input("asdfasdf: "))

#    if choice == 1:

#        editUser()

import math

for i in range(0, 100, 90):
    print(f"{i} {math.sin(math.radians(i)):.2f}", end=" ")


def myth(a, b, c):
    n = 0
    for i in range(a, b + 1):
        if i % c == 0:
            n += 1
    return n


print(myth(3, 10, 4))
list_test[:8:3].reverse()
number1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
number2 = number1[-1::-3]
print(number2)
import random


def gen():
    return random.randrange(2, 101, 2)


for i in range(0, 101):
    print(gen())


x = 1  # 2


def fn1(y=3, z=3):
    return x + y + z  # 2 + 2 + 3 = 7


def fn2(y):
    x = 1
    return x + y  # 8


def fn3(y=3, z=4):
    global x
    x += 1  # 2
    y += 2  # 6
    z += 3  # 7
    return fn1(x), y, fn2(z), z  # 7,6,8,7


print(list(fn3(4)))


def fun():
    return "1", "2"


print(list(fun()))

t = 0
n = 2561
while n > 0:
    # t = 16, n = 256
    t *= 10  # 0 10 160 1650
    t += n % 10  # 1 16 165 1652
    n //= 10  # 256 25 2 0

print(t)  # 1652


sum = 0
for x in range(1, 4, 2):  # [1,3]      x = 1   x = 1   x = 3
    for y in range(2, 5, 2):  # [2,4] #y = 2   y = 4
        for z in range(1, 2, 1):  # [1]z = 1   z = 2
            sum += (x + y) * z  # sum = 3, 8, 13, 20
print(sum)

data = [-1.5, 9, ("engr", (8, "python"), "cn101")]
print(data[2][1][1][3])


def mystery(s: str):
    s = s.lower()
    n = 0

    for c in range(ord("a"), ord("z") + 1):
        if chr(c) in s:
            n += 1

    return n


n = 0
sum = 0
data = [22, 7, 24, 59, 10, 9, -1]
for x in data:  # 22 7 24 59
    while x >= 0:
        if sum < 100:
            n += 1  # 1 2 3 4
            sum += x  # 22 29 53 112
        break

print(n, sum)  # 4 112


def myfn(t: list):
    return t[0][1]


data = [("cat", 2), ("dog", 3), ("ant", 4), ("fish", 1)]
data.sort(key=myfn)
print(data)

t = 0
n = 2561

for c in str(n):
    t += int(c)

print(t)
