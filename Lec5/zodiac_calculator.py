#!/usr/bin/env python3

ans = input("Are you quiet/introverted? ")

if ans.lower() == "yes":
    ans = input('Are you a "Feeler" or a "Thinker"? ')
    if ans.lower() == "thinker":
        ans = input("Are you humanitarian? ")
        if ans.lower() == "yes":
            print("Aquarius")
        else:
            ans = input("Are you the CPA or the CEO of a business? ")
            if ans.lower() == "ceo":
                print("Capricorn")
            elif ans.lower() == "cpa":
                print("Virgo")
            else:
                print("Invalid Input")
    elif ans.lower() == "feeler":
        ans = input("Are you self-confidant? ")
        if ans.lower() == "yes":
            ans = input("Do you want attention? ")
            if ans.lower() == "yes":
                ans = input("Do you always finish what you start? ")
                if ans.lower() == "yes":
                    print("Leo")
                else:
                    print("Aries")
            elif ans.lower() == "kind of":
                print("Gemini")
            else:
                print("Scorpio")
        elif ans.lower() == "sometimes" or ans.lower() == "sometime":
            ans = input("Are you humanitarian? ")
            if ans.lower() == "yes":
                print("Aquarius")
            else:
                ans = input("Are you the CPA or the CEO of a business? ")
                if ans.lower() == "ceo":
                    print("Capricorn")
                elif ans.lower() == "cpa":
                    print("Virgo")
                else:
                    print("Invalid Input")
        else:
            ans = input("Can you say no to people? ")
            if ans.lower() == "yes":
                print("Cancer")
            elif ans.lower() == "sometimes" or ans.lower() == "sometime":
                print("Virgo")
            else:
                ans = input("Are you very flirtatious? ")
                if ans.lower() == "yes":
                    print("Libra")
                else:
                    print("Pisces")

    else:
        print("Invalid Input")
else:
    ans = input("Are you very physical? ")
    if ans.lower() == "yes":
        ans = input("Are you married? ")
        if ans.lower() == "yes":
            print("Taurus")
        elif ans.lower() == "maybe":
            ans = input("Do you always finish what you start? ")
            if ans.lower() == "yes":
                print("Leo")
            else:
                print("Aries")
        else:
            print("Sagittarius")
    else:
        ans = input("Are you self-confidant? ")
        if ans.lower() == "yes":
            ans = input("Do you want attention? ")
            if ans.lower() == "yes":
                ans = input("Do you always finish what you start? ")
                if ans.lower() == "yes":
                    print("Leo")
                else:
                    print("Aries")
            elif ans.lower() == "kind of":
                print("Gemini")
            else:
                print("Scorpio")
        elif ans.lower() == "sometimes":
            ans = input("Are you humanitarian? ")
            if ans.lower() == "yes":
                print("Aquarius")
            else:
                ans = input("Are you the CPA or the CEO of a business? ")
                if ans.lower() == "ceo":
                    print("Capricorn")
                elif ans.lower() == "cpa":
                    print("Virgo")
                else:
                    print("Invalid Input")
        else:
            ans = input("Can you say no to people? ")
            if ans.lower() == "yes":
                print("Cancer")
            elif ans.lower() == "sometimes" or ans.lower() == "sometime":
                print("Virgo")
            else:
                ans = input("Are you very flirtatious? ")
                if ans.lower() == "yes":
                    print("Libra")
                else:
                    print("Pisces")
