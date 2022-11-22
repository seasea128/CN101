#!/usr/bin/env python3

text = "Hello, this is CN101"
result = ""

for ch in text:
    if ch.isdigit():
        result += ch

print(result)

result = text.replace("Hello", "Goodbye")

print(result)

date_string = "22/11/2022"

[d, m, y] = date_string.split("/")

print(f"{y}-{m}-{d}")

text = ""
for count in range(1, 5):
    text += "Z" * count + "\n"

for count in range(5, 1, -1):
    text += "Z" * count + "\n"

print(text)

text = "Today is Tuesday."
# for index in range(len(text)):
#     if index % 2 == 0:
#         print(text[index], end="")

# Output = "Tdyi usa."

print(text[-1:0:-2])

text = "Chanon Yothavut"
text = ", ".join(text.split(" ")[::-1])
print(text)

list = ["1", "2", "3"]
tuples = tuple(list)
print(tuples)

ROW = 3
COL = 3
mul_table = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for r in range(ROW):
    for j in range(COL):
        if r == j:
            mul_table[r][j] = (r + 1) * (j + 1)
print(mul_table)


mul_table = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mul_table[0].reverse()
mul_table[1].remove(5)
mul_table[2].append(10)  # Output [10,9,8,7]
mul_table[2].reverse()
print(mul_table)

mul_table = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

x = mul_table[mul_table[0][1]][mul_table[0][0]]  # x = out of range
print(x)


def a(b=5):
    return b * b


def c(d=6):
    return d * 2


print(c(a(2)))  # Output 50


import math

y = 3
z = 4
x = (
    math.exp(math.log10(math.sqrt(math.pow(math.sin(y), 2) + math.pow(math.cos(z), 2))))
    / 2
)


def abc(y, x=2, z=0):
    return x**2 + y + z


print(abc(y=1, z=1))

PRICE = 1


def calculate_cola(quantity):
    if quantity > 10:
        return [10, quantity * PRICE * 0.9]
    else:
        return [0, quantity * PRICE]


def calculate_candy(quantity):
    if quantity > 20:
        return [20, quantity * PRICE * 0.8]
    else:
        return [0, quantity * PRICE]


def calculate_discount(item, quantity):
    match (item):
        case 1:
            return calculate_cola(quantity)
        case 2:
            return calculate_candy(quantity)
