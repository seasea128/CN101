#!/usr/bin/env python3


def check_day(day):
    day_index = day % 7
    if day_index == 1:
        return "Sunday"
    elif day_index == 2:
        return "Monday"
    elif day_index == 3:
        return "Tuesday"
    elif day_index == 4:
        return "Wednesday"
    elif day_index == 5:
        return "Thursday"
    elif day_index == 6:
        return "Friday"
    elif day_index == 0:
        return "Saturday"
    else:
        return "Something is not right"


for x in range(1, 31):
    day = check_day(x)
    print(x, day)
