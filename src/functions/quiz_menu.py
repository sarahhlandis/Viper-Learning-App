from functions.terminal import clear_terminal
from functions.user_input import handleUserInput

# MENU ONCE IN QUIZ MODE

def quiz_menu():

    print('''\nWould you like to continue?
        Press 1 to Continue in Quiz Mode
        Press 2 for Learning Mode 
        Press 3 for Translator Mode
        Type \home to return Home
        Type \exit to Exit at any time \n''')

    while True:
        option = handleUserInput("What would you like to do? \n")
        if option == "1":
            clear_terminal()
            print("Welcome Back!\n")
            from functions.quiz import quiz
            quiz()
        elif option == "2":
            from functions.learning_mod import learning
            clear_terminal()
            learning()
        elif option == "3":
            clear_terminal()
            from functions.translator import translator
            translator()
        else:
            print('''\nThat's not a valid menu option. Please try again
            from the selection above.\n''')