#!/usr/bin/env python3

p1 = input("Player 1 enter: ")
p2 = input("Player 2 enter: ")

if p1 == p2:
    print("Draw")

# scissor vs paper
elif p1 == "s" and p2 == "p":
    print("P1 wins")
elif p2 == "s" and p1 == "p":
    print("P2 wins")

# rock vs scissor
elif p1 == "r" and p2 == "s":
    print("P1 wins")
elif p2 == "r" and p1 == "s":
    print("P2 wins")

# paper vs rock
elif p1 == "p" and p2 == "r":
    print("P1 wins")
elif p2 == "p" and p1 == "r":
    print("P2 wins")
