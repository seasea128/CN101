#!/usr/bin/env python3
list = []
choice = 99


def print_operation():
    print("1. Add")
    print("2. Search")
    print("3. Edit")
    print("4. Calculate Age")
    print("5. Show information")


def add():
    new_info = input(
        "Enter info (format: ID, name, last name, dob, phonenumber): "
    ).split(",")
    if len(new_info) != 5:
        print("Input invalid: not according to format")
        return
    for info in list:
        if info == new_info:
            print("Record already exist")
            return

    list.append(new_info)
    print("Add success")


def search():  # Need more detail
    id = input("Enter ID to search with: ")
    for row in list:
        if row[0] == id:
            print(f"Result: {row}")
        else:
            print("No row matched with ID")


def age():
    index = int(input("Enter the index of record you want to calculate age: "))
    if index >= len(list):
        print("Index is out of bound")
        return

    current_year = 2022
    birth_year = int(list[index][3].split("/")[2])

    print(f"Age: {current_year-birth_year}")


def edit():
    index = int(input("Enter the index of record you want to edit: "))
    if index >= len(list):
        print("Index is out of bound")
        return

    new_info = input(
        "Enter info (format: ID, name, last name, dob, phonenumber): "
    ).split(",")
    if len(new_info) != 5:
        print("Input invalid: not according to format")
        return
    list[index] = new_info
    print("Edit Success")


def show_info():
    index = int(input("Enter index of the record: "))
    if index >= len(list):
        print("Index is out of bound")
        return
    split_dob = list[index][3].split("/")
    censored_dob = f"**/{split_dob[1]}/{split_dob[2][:3]}*"
    phone = list[index][4]
    censored_phone = f"{phone[:6]}{'*'*(len(phone)- 6)}"

    print(
        f"{list[index][1]} {list[index][2]} DOB: {censored_dob} Phone number: {censored_phone}"
    )


while choice != 0:
    print_operation()
    choice = int(input("Enter selection: "))
    if choice == 1:
        add()
    elif choice == 2:
        search()
    elif choice == 3:
        edit()
    elif choice == 4:
        age()
    elif choice == 5:
        show_info()
    else:
        print("Invalid operation")
