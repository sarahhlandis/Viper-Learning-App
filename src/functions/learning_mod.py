import csv
import random

from functions.learning_menu import learning_menu
from functions.terminal import clear_terminal
from pathlib import Path
from functions.user_input import *

def learning():

    def learning_mode(file_to_open, language_to_practice):

        with open(file_to_open) as readFile:
            open_file = csv.reader(readFile)
            vocabulary = list(open_file)    # convert file to list of lists (per row)
            word_check(vocabulary, language_to_practice)    # pass list and lang to func

    # Initialize empty list to store correct and incorrect values
    correct = []
    incorrect = []

    def word_check(vocabulary, language_to_practice):

        list_len = len(vocabulary)-1
        counter = 0

        # statement assigns index of opposite lang word (display practice word)
        if language_to_practice == "english":
            lang_index = 1
        else:
            lang_index = 0

        # statement switches the index to correspond with language of their answer, 
        # to determine if a match (correct)
        if lang_index == 1:
            guessword = 0
        else: guessword = 1

        studying_language = vocabulary[0][lang_index]
        #vocabulary[0][1] gives french value
        #vocabulary[0][0] gives english value
        # these are the header rows in the csv file


        while counter < list_len:  # # # this loop runs past list length by 1! # # #
            random_word = random.randint(1,
                                        list_len)  # figure out how gen random int
            # # without repeating one that has already occurred

            #generates index of random practice word relative to lang chosen
            practice_word = vocabulary[random_word][lang_index]
            counter+=1

            # tries = 0
            x=3
            for tries in range(1, 4):
                user_entry = (handleUserInput(
                    f"What is the {language_to_practice} translation of {practice_word}?\n"
                )).lower()
                # tries += 1 # to iterate up to 3 tries (inclusive)
                x-=1 # to show tries left on output of each guess (when wrong)
                if user_entry == (vocabulary[random_word][guessword]).lower():
                    print("Nice work! That's correct. \n")
                    break  # (break loop if correct)
                    # return correct.append(practice_word)    # return correct word to list
                elif user_entry != (vocabulary[random_word][guessword]).lower():
                    print(
                        f"Incorrect. You have {x} tries remaining! \n"
                    )
                    # return incorrect.append(practice_word)
            # if counter==list_len:
            #     break
        learning_menu()
        

    # Translate mode opening greeting message
    print('''\nYou're now in Viper Learning Mode. Please follow the below
    prompts to get started - \n''')

    # Get user input to determine which language as base study
    practice_lang = handleUserInput_stringOnly(
        '''\nIf you wish to study from foreign language translations (note: this 
        will require you to respond in eng), type English.\n 
        If you wish to study from english translations (note: this 
        will require you to respond in foreign lang), type Foreign: \n''')



    clear_terminal() # Clear terminal before user enters file name

    # Allow user input to choose which file they wish to study
        # Create path that represents the current directory
    target_dir = Path('.')
    filename = handleUserInput("Please enter the filename you wish to study: \n").lower()
    # searches thru files and returns matching
    filepath = list(Path(target_dir).glob(f"**/{filename}.csv"))[0]


    # determine user input to run correct func
    if practice_lang.lower() == "english":
        print("\n")
        learning_mode(filepath, practice_lang.lower())

    if practice_lang.lower() == "foreign":
        print("\n")
        learning_mode(filepath, practice_lang.lower())



# To resolve
# error handling
# output percentage of correctly answered. list accessibility/break statements?
# random gen without repeating
# code in keyboardInterrupt \quit option

