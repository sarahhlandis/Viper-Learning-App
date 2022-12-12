# import googletrans
# import textblob
# import random
# import os 
from time import sleep
from sys import exit

from functions.terminal import clear_terminal


# Opening Greeting with Menu Options
clear_terminal()
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
                clear_terminal()
                from functions.translator import translator
                translator()
        if option == "2":
                clear_terminal()
                from functions.learning_mod import learning
                learning()
        if option == "3":
                clear_terminal()
                from functions.quiz2 import quiz
                quiz()
if option=="\exit":
        print ("\n Thanks for learning. Come back soon to pick up where you left off! \n")
        exit(0)

# code in try/except block for invalid entries.. 
# review while loop
# code the raise keyboardinterrupt - \exit
