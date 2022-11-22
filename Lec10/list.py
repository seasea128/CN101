#!/usr/bin/env python3

students = []

choice = 10


def print_operation():
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
    print("10: Compare between two values")
    print("11: Search and replace name/lastname")  # TODO: Implement this
    print("0: Exit the program")


def search_and_replace():
    search_type = (
        int(input("Enter variable to search for (1 = First Name, 2 = Last Name): ")) - 1
    )
    search_query = input("Enter name to search for: ")
    replace = input("Enter name to replace: ")
    for row in students:
        name = row[1].split(" ")
        if name[search_type].find(search_query) != -1:
            row[1] = row[1].replace(search_query, replace)
            break  # Only change first record found

    print(students)


def append_item():
    student = input("Enter data (format: ID,Name,GPA): ").split(",")
    for row in students:
        if row[0] == student[0]:
            print(f"Duplicate Student ID at index {students.index(row)}")
            return

    students.append(student)
    print("Append success")


def insert_item():
    student = input("Enter data (format: ID,Name,GPA): ").split(",")
    for row in students:
        if row[0] == student[0]:
            print(f"Duplicate Student ID at index {students.index(student)}")
            return

    index = int(input("Enter index: "))
    students.insert(index, student)
    print(f"Insert Student ID {student} at index {index} success")


def search():
    type = int(input("Enter variable to search (1=ID, 2=Name, 3=GPA): "))
    if type == 1:
        search_by_id()
    elif type == 2:
        search_by_name()
    elif type == 3:
        search_by_gpa()


def search_by_id():
    id = int(input("Enter Student ID: "))
    for row in students:
        if row[0] == id:
            item = students.index(row)
            print(f"Student ID: {id} is at index {item}")
        else:
            print(f"Student does not exist")


def search_by_name():
    name = input("Enter name: ").lower()
    for row in students:
        if row[1].lower() == name:
            item = students.index(row)
            print(f"Name: {name} is at index {item}")
        else:
            print(f"Student does not exist")


def search_by_gpa():
    [gpa_min, gpa_max] = input("Enter GPA range split by comma: ").split(",")
    output = []
    for row in students:
        if row[2] < float(gpa_max) & row[2] > float(gpa_min):
            output.append(row)

    if len(output) == 0:
        print("No student found")
        return

    print(f"Result: {output}")


def print_list():
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


def remove_item_with_id():
    id = int(input("Enter Student ID: "))
    for row in students:
        if row[0] == id:
            students.remove(row)
            print("Remove success")
            return


def remove_item_with_index():
    index = int(input("Enter index: "))
    if index > (len(students) - 1):
        print("Index is larger than the size of the list")
    else:
        del students[index]
        print("Remove success")


def sort():
    sort = int(input("Enter variable to sort by (1 = ID, 2 = Name, 3 = GPA): "))
    if sort == 1:
        sort_by_id()
    elif sort == 2:
        sort_by_name()  # Broken
    elif sort == 3:
        sort_by_gpa()  # Broken
    else:
        print("Selection invalid")


def sort_by_gpa():
    sort = int(
        input("Enter direction of sorting (1 = Small to large, 2 = Large to small): ")
    )
    if sort == 1:
        students.sort(key=lambda x: x[2])
        print("Sorting success")
    elif sort == 2:
        students.sort(key=lambda x: x[2])
        students.reverse()
        print("Sorting success")
    else:
        print("Selection invalid")


def sort_by_name():
    sort = int(
        input("Enter direction of sorting (1 = Small to large, 2 = Large to small): ")
    )
    if sort == 1:
        students.sort(key=lambda x: x[1])
        print("Sorting success")
    elif sort == 2:
        students.sort(key=lambda x: x[1])
        students.reverse()
        print("Sorting success")
    else:
        print("Selection invalid")


def sort_by_id():
    sort = int(
        input("Enter direction of sorting (1 = Small to large, 2 = Large to small): ")
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


def reverse():
    students.reverse()
    print("Reverse success")


def sum_min_max_gpa():
    sum = 0
    max = 0
    min = 9999999999999999
    for student in students:
        if student[2] > max:
            max = student[2]
        if student[2] < min:
            min = student[2]
        sum += student[2]
    print(f"Minimum value: {min}")
    print(f"Maximum value: {max}")
    print(f"Sum of value: {sum}")
    print(f"Average of value: {sum / len(students)}")


def compare():
    choice = int(input("Enter variable to compare by (1 = ID, 2 = Name, 3 = GPA): "))
    if choice == 1:
        compare_by_id()
    elif choice == 2:
        compare_by_name()
    elif choice == 3:
        compare_by_gpa()


def compare_by_id():
    index1 = int(input("Enter index of first value to be compare: "))
    if index1 > len(students):
        print("Index is larger than the size of the list")
    index2 = int(input("Enter index of second value to be compare: "))
    if index2 > len(students):
        print("Index is larger than the size of the list")
    if students[index1][0] == students[index2][0]:
        print(f"ID {students[index1][0]} is equal to ID {students[index2][0]}")
    elif students[index1][0] > students[index2][0]:
        print(f"ID {students[index1][0]} is greater than ID {students[index2][0]}")
    elif students[index1][0] < students[index2][0]:
        print(f"ID {students[index1][0]} is less than ID {students[index2][0]}")


def compare_by_name():
    index1 = int(input("Enter index of first value to be compare: "))
    if index1 > len(students):
        print("Index is larger than the size of the list")
    index2 = int(input("Enter index of second value to be compare: "))
    if index2 > len(students):
        print("Index is larger than the size of the list")
    if students[index1][1] == students[index2][1]:
        print(f"Name {students[index1][1]} is equal to Name {students[index2][1]}")
    elif students[index1][1] > students[index2][1]:
        print(f"Name {students[index1][1]} is greater than Name {students[index2][1]}")
    elif students[index1][1] < students[index2][1]:
        print(f"Name {students[index1][1]} is less than Name {students[index2][1]}")


def compare_by_gpa():
    index1 = int(input("Enter index of first value to be compare: "))
    if index1 > len(students):
        print("Index is larger than the size of the list")
    index2 = int(input("Enter index of second value to be compare: "))
    if index2 > len(students):
        print("Index is larger than the size of the list")
    if students[index1][2] == students[index2][2]:
        print(f"GPA {students[index1][2]} is equal to GPA {students[index2][2]}")
    elif students[index1][2] > students[index2][2]:
        print(f"GPA {students[index1][2]} is greater than GPA {students[index2][2]}")
    elif students[index1][2] < students[index2][2]:
        print(f"GPA {students[index1][2]} is less than GPA {students[index2][2]}")


while choice != 0:
    print_operation()
    choice = int(input("Enter operation: "))
    print(f"Your choice is {choice}")

    if choice == 1:
        append_item()
    elif choice == 2:
        insert_item()
    elif choice == 3:
        search()
    elif choice == 4:
        print_list()
    elif choice == 5:
        remove_item_with_id()
    elif choice == 6:
        remove_item_with_index()
    elif choice == 7:
        sort()
    elif choice == 8:
        reverse()
    elif choice == 9:
        sum_min_max_gpa()
    elif choice == 10:
        compare()
    elif choice == 11:
        search_and_replace()
    elif choice == 0:
        print("Exiting")
        break
    else:
        print("Invalid operation")
