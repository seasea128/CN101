#!/usr/bin/env python3

import math


def power(x, n):
    return math.exp(n * math.log(x))


a1 = power(4, 0.5)
a2 = power(5.0625, 0.25)
b1 = math.pow(4, 0.5)
b2 = math.pow(5.0625, 0.25)

print(f"a1 = {a1}, a2 = {a2}, b1 = {b1}, b2 = {b2}")
