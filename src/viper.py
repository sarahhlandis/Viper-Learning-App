# from time import sleep
from sys import exit

from functions.terminal import clear_terminal
from functions.user_input import handleUserInput

# MAIN PY FILE

def viper_main():
        # Opening Greeting with Menu Options
        clear_terminal()
        print('''\nWelcome to Viper, your personalized language learning app. Please select which 
                mode you'd like to enter from the options below. 
                Press 1 for Translator Mode 
                Press 2 for Learning Mode 
                Press 3 for Quiz Mode 
                Type \exit to Exit at any time \n''')

        while True:
        # Menu Options from Start
                option = handleUserInput("\nWhat would you like to do? \n")
                # while option!="\exit":
                if option == "1":
                        clear_terminal()
                        from functions.translator import translator
                        translator()
                elif option == "2":
                        clear_terminal()
                        from functions.learning_mod import learning
                        learning()
                elif option == "3":
                        clear_terminal()
                        from functions.quiz import quiz
                        quiz()
                else: 
                        print('''\nThat's not a valid menu option. Please try again
                        from the selection above.''')
                        

viper_main()

