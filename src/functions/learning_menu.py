from functions.terminal import clear_terminal
from functions.quiz import quiz
from functions.user_input import handleUserInput

# Menu once already in Learning Mode
def learning_menu():
    print('''\nWould you like to continue?
        Press 1 to Continue in Learning Mode
        Press 2 for Translator Mode 
        Press 3 for Quiz Mode
        Type \home to return Home
        Type \exit to Exit at any time \n''')

    option = handleUserInput("What would you like to do? \n")
    # if option!="\exit":
    if option == "1":
        clear_terminal()
        print("\nWelcome Back!\n")
        from functions.learning_mod import learning
        learning()
    if option == "2":
        clear_terminal()
        from functions.translator import translator
        translator()
    if option == "3":
        clear_terminal()
        quiz()
    # elif option=="\exit":
    #         print ("\nThanks for learning. Come back soon to pick up where you left off!\n")
    #         exit(0)