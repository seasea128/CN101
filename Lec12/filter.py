#!/usr/bin/env python3
word_list = []

choice = 99


def print_operation():
    print("Choose from menu: ")
    print("1) Show the list of inappropriate words")
    print("2) Add new words")
    print("3) Remove words")
    print("4) Filter out a message")


def show_list():
    print(f"Your list is {word_list}")


def add():
    added_word = input("Enter words to add (separated by comma): ").split(",")
    global word_list
    for add in added_word:
        for word in word_list:
            if add == word:
                print("Operation aborted, word already in list")
                return

    word_list += added_word
    print("Adding success")


def remove():
    remove_word = input("Enter words to remove (separated by comma): ").split(",")
    for remove in remove_word:
        for word in word_list:
            if remove == word:
                word_list.remove(word)

    print("Remove success")


def message_filter():
    sentence = input("Enter a sentence: ")
    for word in word_list:
        position = sentence.find(word)
        if position != -1:
            replace_str = word[0] + "*" * (len(word) - 2) + word[-1]
            sentence = sentence.replace(word, replace_str)

    print(sentence)


while choice != 0:
    print_operation()

    choice = int(input("Enter selection: "))
    if choice == 1:
        show_list()
    elif choice == 2:
        add()
    elif choice == 3:
        remove()
    elif choice == 4:
        message_filter()
