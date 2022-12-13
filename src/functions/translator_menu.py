from functions.terminal import clear_terminal
from functions.user_input import handleUserInput

# Menu once in Translator
def translator_menu():
    print('''\nWould you like to continue?
        Press 1 to Continue in Translator Mode
        Press 2 for Learning Mode 
        Press 3 for Quiz Mode
        Type \exit to Exit at any time\n''')
        # Type \home to Return to the main menu

    option = handleUserInput("What would you like to do? \n")
    # if option!="\exit":
    if option == "1":
        clear_terminal()
        print("Welcome Back!\n")
        from functions.translator import translator
        translator()
    if option == "2":
        from functions.learning_mod import learning
        clear_terminal()
        learning()
    if option == "3":
        clear_terminal()
        from functions.quiz import quiz
        quiz()
    # elif option=="\exit":
    #         print ("Thanks for learning. Come back soon to pick up where you left off!\n")
    #         exit(0)
