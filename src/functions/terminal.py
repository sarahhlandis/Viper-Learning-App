import os 

# function to clear terminal

def clear_terminal():
    print(os)
    if os.name == "nt": # If the user is on windows
        _ = os.system("cls") # run `cls`
    else:
        _ = os.system("clear") # If the user is on Mac/linux, run clear