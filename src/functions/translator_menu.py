from functions.terminal import clear_terminal
from functions.user_input import handleUserInput

# MENU ONCE IN TRANSLATOR

def translator_menu():
    print('''\nWould you like to continue?
        Press 1 to Continue in Translator Mode
        Press 2 for Learning Mode 
        Press 3 for Quiz Mode
        Type \home to return Home
        Type \exit to Exit at any time\n''')

    option = handleUserInput("What would you like to do? \n")
    
    if option == "1":
        clear_terminal()
        print("Welcome Back!\n")
        from functions.translator import translator
        translator()
    elif option == "2":
        from functions.learning_mod import learning
        clear_terminal()
        learning()
    elif option == "3":
        clear_terminal()
        from functions.quiz import quiz
        quiz()
   
