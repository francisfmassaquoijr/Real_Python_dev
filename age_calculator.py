# Important libraries that will help the program run smoothly 
from __future__ import print_function 

# author's info 
__author__ = "Francis F. Massaquoi, Jr."

# age calculator 

usr_name = str(raw_input("Hi, what is your name? "))
print("Nice meeting you", usr_name)

while True:
	try:
		birth_yrl = int(raw_input("What is your year of birth? "))
	except ValueError:
		print(usr_name, "please enter your year of birth ex: 1998")
	else: 
		break 

while True:
	try:
		curr_yrl = int(raw_input("What is the current year? "))
	except ValueError:
		print(usr_name, "please enter the current year to continue")
	else:
		break 

usr_age = int(birth_yrl) - int(curr_yrl)
print("Hi ", usr_name, "you're ", usr_age, "years of age, thanks for using our program to calculate your age")
raw_input("Press enter to exit")

