"""
File: print.py
================
Prints general information about the program.

"""

import string


"""
Function: welcome
===================
Introduces the user to Otero Assassins.

"""
def welcome():
    print("Welcome to Otero Assassins!")
    print("Would you like to watch as an entire dorm gets killed off one by one?")
    print("Well, you can't.")
    print("But enjoy this animation of a bunch of nodes dying off in lieu of the actual thing!")
    instruction()


"""
Function: instruction
======================
Prompts the user for whether or not to print the general rules for Assassins.

"""
def instruction():
    instruction = input("Before we start, would you like a quick overview of the game? Y/N ")
    instruction = instruction.lower()
    while (instruction != "y" and instruction != "n"):
        print("Sorry, please enter either 'Y' or 'N':")
        instruction = input("Would you like a quick overview of the game? Y/N ")
    if instruction == "n":
        print("\nGreat! Let's get started!\n")
    elif instruction == "y":
        print("\nGreat! Here's how Assassins works:\n")
        assassins()


"""
Function: assassins
====================
Prints the rules for Assassins.

"""
def assassins():
    print("Assassins is a live-action game in which players try to eliminate one another using mock weapons.")
    print("Each player has a specific target, and their role is to track and eliminate that target.")
    print("Once the player has eliminated their target, they proceed to track their victim's target.")
    print("The game is over when there is only one player remaining.\n")


"""
Function: start
================
Delays the program until the user is ready to start.

"""
def start():
    start = input("Ready to start? Press enter. ")
