import googletrans
import textblob
import random
import os 
from time import sleep
from sys import exit

from functions.translator import translator
from functions.translator_menu import translator_menu, translator
from functions.learning import english

# Opening Greeting with Menu Options
print('''\n Welcome to Viper, your personalized language learning app. Please select which 
        mode you'd like to enter from the options below. 
        Press 1 for Translator Mode 
        Press 2 for Learning Mode 
        Press 3 for Quiz Mode 
        Type \exit to Exit at any time \n''')

# Menu Options from Start
option = input("What would you like to do? \n")
while option!="\exit":
        if option == "1":
                print("\n")
                translator()
                translator_menu()
        if option == "2":
                print("\n")
                english()
        if option == "3":
                pass
        elif option=="\exit":
                print ("Thanks for learning. Come back soon to pick up where you left off!\n")
                exit()

# code in try/except block for invalid entries.. 
# review while loop
# code the raise keyboardinterrupt - \exit
