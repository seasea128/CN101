#!/usr/bin/env python3

import math

width = float(input("Input the width of the aquarium: "))
length = float(input("Input the length of the aquarium: "))
height = float(input("Input the height of the aquarium: "))
radius = float(input("Input the radius of the walkway: "))

aquariumVol = width * length * height
walkwayVol = math.pi * (radius**2) * length

print(f"\nThe amount of water needed is {aquariumVol - walkwayVol:.3f} cubic meters")
