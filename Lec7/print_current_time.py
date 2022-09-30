#!/usr/bin/env python3

from time import sleep
from os import system

hour = 0
minute = 0
second = 0

for hour in range(24):
    for minute in range(60):
        for second in range(60):
            print(
                f"{hour:2d}",
                f"{minute:2d}",
                f"{second:2d}",
                sep=":",
            )
            sleep(0.1)
            system("clear")
