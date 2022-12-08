import googletrans
import textblob
import random
from sys import exit

from functions.translator import translator

# Introduction Menu
print('''\n Welcome to Viper, your personalized language learning app. Please select which 
        mode you'd like to enter. 
        Press 1 for Translator Mode 
        Press 2 for Learning Mode 
        Press 3 for Quiz Mode 
        Press E to Exit at any time \n''')

# Menu Options
option = input("What would you like to do? \n")
while option!="E":
        if option == "1":
                translator()
        if option == "2":
                pass
        if option == "3":
                pass
if option=="E":
        print ("Thanks for learning. Come back soon to pick up where you left off!\n")
        quit()

       

