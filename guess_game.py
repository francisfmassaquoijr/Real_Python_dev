from __future__ import print_function
import random

# author's info
__author__ = "Francis F. Massaquoi, Jr."

def numb_guesser():
    # validating username
    while True:
        usr_name = str(raw_input("Hi, what is your username: "))
        if usr_name.isalpha() == True:
            print("Welcome ", usr_name, "nice meeting you........")
            break
        else:
            print("Please enter only username no spaces, numbers, or symbols")
            continue

    # magic number
    mag_num = random.randint(1, 10)
    quit_app = raw_input("Do you want to play magic number game? Press 'y' to play, and 'q' to quit: ")
    while quit_app != 'q' or quit_app != 'Q':
        usr_ques = raw_input("What is the magic number? ")
        if usr_ques == mag_num:
            print("Yes", usr_name, "you got the magic number, you're a genius")
        elif usr_ques > mag_num:
            print("You guess is too hard, try again.....")
        elif usr_ques < mag_num:
            print("Your guess is less, try again..")
        else:
            print("Sorry try again ")

numb_guesser()
