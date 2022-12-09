import csv
import random
import os 



# Allow user input to choose which file they wish to study
filename = input("File you wish to study: ").lower()

# All user input to determine which language as base study
practice_lang = input('''If you wish to study english translations, type English. 
    If you wish to study the foreign language translations, type Foreign: ''') 

# Initialize empty list to store correct and incorrect values
correct = []
incorrect = []

def english():
    # Read's user's specified CSV file and stores in new dictionary
    with open(filename) as readFile:
        open_file = csv.reader(readFile)
        # vocabulary=list(map(tuple, open_file))
        vocabulary=list(open_file)
        print (vocabulary)
        # below prints english word pair value
        print(vocabulary[12][0])
        # below prints french word pair value
        print(vocabulary[12][1])
        # below prints total length of list incl. header row
        print(len(vocabulary)-1)

        list_len=len(vocabulary)-1
        counter=0

        def word_check1():
            while counter <= list_len:
                random = random.randint(1,list_len) # figure out how gen random int
                # without repeating one that has already occurred
                english_word=vocabulary[random][0]
                user_entry=(input(f"What is the {vocabulary[0][1]} translation of {english_word}?\n"))
                
                tries=0
                for tries in range(1-4):   # for loop for capped # of guesses. for loop
                # not activating..
                    tries+=1
                    if user_entry==(vocabulary[random][1]):
                        print("Nice work! That's correct. ")
                    elif user_entry!=(vocabulary[random][1]):
                        print("Try again! ")
                    continue
        word_check1()

    english()


# for studying in french instead
def french():
    # Read's user's specified CSV file and stores in new dictionary
    with open(filename) as readFile:
        open_file = csv.reader(readFile)
        # vocabulary=list(map(tuple, open_file))
        vocabulary=list(open_file)
        print (vocabulary)
        # below prints english word pair value
        print(vocabulary[12][0])
        # below prints french word pair value
        print(vocabulary[12][1])
        # below prints total length of list incl. header row
        print(len(vocabulary)-1)

        list_len=len(vocabulary)-1
        counter=0

        def word_check2():
            while counter <= list_len:
                random = random.randint(1,list_len) # figure out how gen random int
                # without repeating one that has already occurred
                french_word=vocabulary[random][1]
                user_entry=(input(f"What is the {vocabulary[0][0]} translation of {french_word}?\n"))
                
                tries=0
                for tries in range(1-4):   # for loop for capped # of guesses. for loop
                # not activating..
                    tries+=1
                    if user_entry==(vocabulary[random][0]):
                        print("Nice work! That's correct. ")
                    elif user_entry!=(vocabulary[random][0]):
                        print("Try again! ")
                    continue
        word_check2()

    french()

# determine user input to run correct func
if practice_lang=="english".lower():
    english()
if practice_lang=="foreign".lower():
    french()
