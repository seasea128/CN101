#!/usr/bin/env python3

students = []

choice = 10

while choice != 0:
    print("What operation do you want to do")
    print("1: Append item to list.")
    print("2: Insert item to list.")
    print("3: Search item in the list")
    print("4: Show item in the list")
    print("5: Remove item with ID")  # Implemented
    print("6: Remove item with index")  # Implemented
    print("7: Sort item in the list")  # Implemented
    print("8: Reverse list")  # Implemented
    print("9: Find min, max, sum, and average")
    print("0: Exit the program")
    choice = int(input("Enter operation: "))
    print(f"Your choice is {choice}")

    if choice == 1:
        item = int(input("Enter Student ID: "))
        if item in students:
            print(f"Duplicate Student ID at index {students.index(item)}")
        else:
            students.append(item)
            print("Append success")
    elif choice == 2:
        item = int(input("Enter Student ID: "))
        if item in students:
            print(f"Duplicate Student ID at index {students.index(item)}")
        else:
            index = int(input("Enter index: "))
            students.insert(index, item)
            print(f"Insert Student ID {item} at index {index} success")
    elif choice == 3:
        search = int(input("Enter item: "))
        item = students.index(search)
        print(f"Student {search} is at index {item}")
    elif choice == 4:
        selection = int(
            input(
                "Do you want to print all or print a portion of the list? (1 for print all, 2 for print portion): "
            )
        )
        if selection == 1:
            print(students)
        elif selection == 2:
            startRange = int(input("Enter the start of the range: "))
            endRange = int(input("Enter the end of the range: "))
            for x in range(startRange - 1, endRange):
                print(students[x], end=", ")
            print("")
    elif choice == 5:
        item = int(input("Enter Student ID: "))
        if item not in students:
            print(f"Student ID {item} not exist in the list")
        else:
            students.remove(item)
            print("Remove success")
    elif choice == 6:
        index = int(input("Enter index: "))
        if index > len(students):
            print("Index is larger than the size of the list")
        else:
            del students[index]
            print("Remove success")
    elif choice == 7:
        sort = int(
            input(
                "Enter direction of sorting (1 = Small to large, 2 = Large to small): "
            )
        )
        if sort == 1:
            students.sort()
            print("Sorting success")
        elif sort == 2:
            students.sort()
            students.reverse()
            print("Sorting success")
        else:
            print("Selection invalid")
    elif choice == 8:
        students.reverse()
        print("Reverse success")
    elif choice == 9:
        print(f"Minimum value: {min(students)}")
        print(f"Maximum value: {max(students)}")
        print(f"Sum of value: {sum(students)}")
        print(f"Average of value: {sum(students)/ len(students)}")
    elif choice == 0:
        print("Exiting")
        break
    else:
        print("Invalid operation")
