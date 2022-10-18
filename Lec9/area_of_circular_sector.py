#!/usr/bin/env python3

import math


def area_of_circular_sector(r, d):
    return (d / 360) * (math.pi * (r**2))


area_1 = area_of_circular_sector(10, 90)
area_2 = area_of_circular_sector(10, 180)

print(f"Area 1 = {area_1:.2f}, Area 2 = {area_2:.3f}")
