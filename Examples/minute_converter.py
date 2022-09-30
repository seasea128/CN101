#!/usr/bin/env python3

minutes = int(input("Enter minutes: "))

# months = minutes // 43200
# minutes %= 43200
# days = minutes // 1440
# minutes %= 1440
# hours = minutes // 60
# minutes %= 60

months = minutes // 43200  # divide by minutes in months
days = (
    minutes % 43200 // 1440
)  # mod by minutes in months then divide by minutes in days
hours = minutes % 1440 // 60  # mod by minutes in day then divide by minutes in hours
minutes = minutes % 60  # mod by minutes in hours

print(months, days, hours, minutes)
