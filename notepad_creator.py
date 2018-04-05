from __future__ import print_function 

# author's info 
__author__ = "Francis F. Massaquoi, Jr."
'''
writable_file = open("Fred Zoe'spad", 'w')
writable_file.write("Welcome to Fred Zoe'spad")
writable_file.write("you only need to change the text from here.....")
writable_file.close()
'''
readable_file = open("Fred Zoe'spad", 'r')
store_read_file = readable_file.read()
print(store_read_file)
readable_file.close()
