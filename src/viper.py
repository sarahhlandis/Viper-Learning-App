# import googletrans
# import textblob
# import random
# import os 
from time import sleep
from sys import exit

from functions.translator import translator
from functions.translator_menu import translator_menu

# Opening Greeting with Menu Options
print('''\nWelcome to Viper, your personalized language learning app. Please select which 
        mode you'd like to enter from the options below. 
        Press 1 for Translator Mode 
        Press 2 for Learning Mode 
        Press 3 for Quiz Mode 
        Type \exit to Exit at any time \n''')

# Menu Options from Start
option = input("\nWhat would you like to do? \n")
while option!="\exit":
        if option == "1":
                print("\n")
                translator()
                translator_menu()
        if option == "2":
                print("\n")
                from functions import learning_mod
                learning_mod
        if option == "3":
                from functions import quiz2
                quiz2
if option=="\exit":
        print ("\n Thanks for learning. Come back soon to pick up where you left off! \n")
        exit()

# code in try/except block for invalid entries.. 
# review while loop
# code the raise keyboardinterrupt - \exit
