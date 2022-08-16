#! /usr/bin/python3

# salary = int(input("Enter salary: "))
# bonus =  int(input("Enter bonus: "))
# 
# total_pay = salary + bonus
# 
# print(f"Your pay is {total_pay}")

total_seconds = float(input("Enter number of seconds: "))

hours = total_seconds // 3600

minutes = (total_seconds // 60) % 60

seconds = total_seconds % 60

print("Hours:", hours)
print("Minutes:",minutes)
print("Seconds:",seconds)
