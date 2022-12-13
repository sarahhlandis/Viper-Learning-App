from functions.terminal import clear_terminal
from functions.user_input import handleUserInput

# Menu once in Quiz Mode
def quiz_menu():

    print('''\nWould you like to continue?
        Press 1 to Continue in Quiz Mode
        Press 2 for Learning Mode 
        Press 3 for Translator Mode
        Type \exit to Exit at any time \n''')

    option = handleUserInput("What would you like to do? \n")
    # if option!="\exit":
    if option == "1":
        clear_terminal()
        print("Welcome Back!\n")
        from functions.quiz2 import quiz
        quiz()
    if option == "2":
        from functions.learning_mod import learning
        clear_terminal()
        learning()
    if option == "3":
        clear_terminal()
        from functions.translator import translator
        translator()
    # elif option=="\exit":
    #         print ("\nThanks for learning. Come back soon to pick up where you left off!\n")
    #         exit(0)