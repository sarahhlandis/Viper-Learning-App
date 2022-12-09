from functions.translator import translator

# Menu once in Translator
def translator_menu():
    print('''\n Would you like to continue?
        Press 1 to Continue 
        Press 2 for Learning Mode 
        Type \exit to Exit at any time \n''')

    option = input("What would you like to do? \n")
    if option!="\exit":
        if option == "1":
            print("Please follow the prompts below to translate.\n")
            translator()
            translator_menu()
        if option == "2":
            pass
    elif option=="\exit":
            print ("Thanks for learning. Come back soon to pick up where you left off!\n")
            quit()
        