import random
from time import *
import csv
import threading
from pathlib import Path
from functions.terminal import clear_terminal
from functions.quiz_menu import quiz_menu

# def quiz():

def quiz_mode(file_to_open):
    with open(file_to_open) as readFile:
        open_file = csv.reader(readFile)
        vocabulary = list(open_file)    # convert file to list of lists (per row)
        quiz_word(vocabulary) # pass list to function

correct=[]
incorrect=[]

def quiz_word(vocabulary):
    quiz_len = len(vocabulary)-1
    score=0

    while quiz_timer>0:
        random_index = random.randint(1,
                                        quiz_len)  # figure out how gen random int
            # # without repeating one that has already occurred
            
        lang_index= random.randint(0,1)

        # to determine if a match (correct)
        if lang_index == 1:
            guessword = 0
        else: guessword = 1

        # generates index of random quiz word
        test_word = vocabulary[random_index][lang_index]

        # compares user guess to corresponding word
        user_entry = (input(
            f"What is the translation of {test_word}?\n"
        )).lower()
        
        # compares user guess to corresponding word
        if user_entry == (vocabulary[random_index][guessword]).lower():
            print(
                f"Correct!\n"
            )
            score+=1
            # correct.append(quiz_word)
        elif user_entry != (vocabulary[random_index][guessword]).lower():
            print(
                f"Incorrect!\n"
            )
            score-=1
            # incorrect.append(quiz_word)


# def countdown():
#     global quiz_timer
#     for x in range(quiz_timer):
#         mins, secs = divmod(quiz_timer, 60)
#         timer = '{:02d}:{:02d}'.format(mins, secs)
#         print(timer, end="\r")
#         sleep(1)
#         quiz_timer -= 1
#     print ("Ding Ding!! Time's up!!")


def countdown():
    global quiz_timer
    while quiz_timer:
        mins, secs = divmod(quiz_timer, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        # print(timer, end="\r")
        sleep(1)
        quiz_timer -= 1
        if quiz_timer==0:
            print("Ding Ding!! Time's up!!")

countdown_thread=threading.Thread(target=countdown)


# Opening Greeting with Menu Options
# Quiz mode entry greeting message
print('''\nYou're now in Viper Quiz Mode. Please follow the below
prompts to get started - \n''')

# Allow user input to choose which file they wish to study
    # Create path that represents the current directory
target_dir = Path('.')
filename = input("Please enter the filename you wish to study: \n").lower()
# searches thru files and returns matching
filepath = list(Path(target_dir).glob(f"**/{filename}.csv"))[0]

quiz_timer=int(input("\nHow much time would you like on the clock(in seconds)? \n"))

ready=input("\nAre you ready to begin? \n")

# determine user input to run correct func
if ready.lower() == "yes":
    clear_terminal() # Clear terminal before user starts quiz
    countdown_thread.start()
    quiz_mode(filepath)
    countdown()
    print("\n")
    quiz_word()
    quiz_menu()
else: print("Please xxxxx")



# To resolve
# Goal - timer running in background but displaying simultaneously
# list setup for correct/incorrect - unaccessed?
# testing
# Error Handling
# quiz menu not printing at end of quiz


