# from functions.translator import translator
# from functions.translator_menu import translator_menu

# Menu once already in Learning Mode
def learning_menu():
    print('''\n Would you like to continue?
        Press 1 to Continue 
        Press 2 for Translator Mode 
        Press 3 for Quiz Mode
        Type \exit to Exit at any time \n''')

    option = input("What would you like to do? \n")
    if option!="\exit":
        if option == "1":
            print("\n Welcome Back!\n")
            from functions import learning_mod
            learning_mod
        if option == "2":
            print("\n")
            from functions.translator import translator
            translator()
            from functions.translator_menu import translator_menu
            translator_menu()
        if option == "3":
            from functions import quiz2
            quiz2
    elif option=="\exit":
            print ("\n Thanks for learning. Come back soon to pick up where you left off!\n")
            quit()


# To Fix
# learning mod not linking - running to endless blank terminal? others working fine