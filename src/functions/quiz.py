import random
from time import *
import csv
import threading
from pathlib import Path

from functions.terminal import clear_terminal
from functions.quiz_menu import quiz_menu
from functions.user_input import *

# QUIZ MODE

def quiz():
    global quiz_timer
    def quiz_mode(file_to_open):
        with open(file_to_open) as readFile:
            open_file = csv.reader(readFile)
            vocabulary = list(open_file)    # convert file to list of lists (per row)
            quiz_word(vocabulary) # pass list to function

    # create empty sets to not display duplicates
    correct=set()
    incorrect=set()

    def quiz_word(vocabulary):
        quiz_len = len(vocabulary)-1
        score=0
        rounds=0
        

        while quiz_timer>0:
            random_index = random.randint(1,
                                            quiz_len)
                
            lang_index= random.randint(0,1)
            rounds+=1
            # to determine if a match (correct)
            if lang_index == 1:
                guessword = 0
            else: guessword = 1

            # generates index of random quiz word
            test_word = vocabulary[random_index][lang_index]
            # played_rounds=1

            # compares user guess to corresponding word
            user_entry = (handleUserInput(
                f"What is the translation of {test_word}?\n"
            )).lower()
            if user_entry == "":
                rounds-=1

            # output when time's up
            if quiz_timer==0:   
                fraction_score=(len(correct))/rounds
                percentage=fraction_score*100
                
                # output based on how many words correct
                if len(correct)==0:
                    print (f'''You did not get any correct. Time to hit the books!! Come back 
                    and try again later.\n''')
                elif percentage >= 90: 
                    print (f"You're a pro who knows their words! You scored {int(percentage)} percent.")
                elif percentage >= 80:
                    # print (f"Well done! - you got {len(correct)} out of {rounds} words correct!")
                    print (f"Well done! - you sccored {int(percentage)} percent.")
                # print (correct)
                elif percentage >=70:
                    print (f'''Nice job - you sccored {int(percentage)} percent.
                    Looks like there's more work to do...''')
                elif percentage < 70:
                    print(f'''Oh no.. you only scored {int(percentage)} percent. Let's go back
                    to studying...''')

                # to print incorrect set of words
                if len(incorrect)>0:
                    print (f"\nCheck out your quiz report to view words you got wrong and more.")
                else: 
                    print ("You did not get any words wrong. It seems you've mastered it!!")

                print('''\nIf you wish to view your quiz report, please look in the local 
                folder of the Viper application.''')

                # generates more in depth quiz report
                with open('quizreport.txt', 'w') as f:
                    f.write(f"Please see below the list of words you translated correctly: ")
                    for word in correct:
                        f.write(f"{word}\n")
                # prints internal menu
                quiz_menu()

            # compares user guess to corresponding word
            if user_entry == (vocabulary[random_index][guessword]).lower():
                print(
                    f"Correct!\n"
                )
                score+=1
                correct.add(test_word)
            elif user_entry != (vocabulary[random_index][guessword]).lower():
                print(
                    f"Incorrect!\n"
                )
                score-=1
                incorrect.add(test_word)


    def countdown():
        global quiz_timer
        while quiz_timer:
            mins, secs = divmod(quiz_timer, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            # print(timer, end="\r")
            sleep(1)
            quiz_timer -= 1
            if quiz_timer==0:
                print('''\nDing Ding!! Time's up!!\nPress enter to see your results.\n''')
                # print (' '.join(incorrect))
                break
        
    

    countdown_thread=threading.Thread(target=countdown)


    # Opening Greeting with Menu Options
    # Quiz mode entry greeting message
    print('''\nYou're now in Viper Quiz Mode. Please follow the below
    prompts to get started - \n''')

    # Allow user input to choose which file they wish to study
        # Create path that represents the current directory
    # target_dir = Path('.')
    # filename = handleUserInput("Please enter the filename you wish to study: \n").lower()
    # # searches thru files and returns matching
    # filepath = list(Path(target_dir).glob(f"**/{filename}.csv"))[0]

    while True:
        try:
            target_dir = Path('.')
            filename = handleUserInput("Please enter the filename you wish to study: \n").lower()
            # searches thru files and returns matching
            filepath = list(Path(target_dir).glob(f"**/{filename}.csv"))[0]
            break
        except IndexError:
            print("\nSorry that file doesn't seem to exist. Please enter a valid file name.\n")


    while True:
        try:
            quiz_timer=int(handleUserInput("\nHow much time would you like on the clock(in seconds)? \n"))
            break
        except ValueError:
            print("\nLooks like that's not a valid time. Please try again.\n")


    ready=handleUserInput_stringOnly("\nAre you ready to begin? \n")

    # determine user input to run correct func
    if ready.lower() == "yes":
        clear_terminal() # Clear terminal before user starts quiz
        countdown_thread.start()
        quiz_mode(filepath)
        countdown()
        print("\n")
        quiz_word()
    elif ready.lower() == "no": 
        print("\nPlease come back when you're ready!")
        quiz_menu()
    else:
        print("\nSorry, your response was invalid.")
        quiz_menu()
   

# To resolve
# finish code in to output populated list quiz scoresheet file with metrics
# if user doesnt enter a value (if timer cuts them off mid question), still counting as a
    # round and affecting score %




