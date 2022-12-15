# TRANSLATOR MODE
import googletrans
import textblob
from colorama import Back, init
# below allows to not have to reset color for prints after colorama
init(autoreset=True)

from functions.translator_menu import translator_menu
from functions.user_input import *


# Get languages from googletrans pkg dictionary
languages=googletrans.LANGUAGES

# Create a list from googletrans dict with values only
language_list=list(languages.values())

# Function for translator
def translator():
    # Translate mode entry message
    print('''You're now in Viper Translate Mode. Please follow the below
        prompts to translate - \n''')

    # Get user input for original language
    original_lang=handleUserInput_stringOnly("Origin language: ").lower()
    for key, value in languages.items():
        if (value==original_lang):
            original_key=key

    # Get user input for desired language
    desired_lang=handleUserInput_stringOnly("Desired language: ").lower()
    for key, value in languages.items():
        if (value==desired_lang):
            desired_key=key

    # Get user input that determines phrase they wish to translate
    sentence=handleUserInput("Enter phrase: ")
    words=textblob.TextBlob(sentence)

    # Translates user text
    translation=words.translate(from_lang=original_key,to=desired_key)
    # Returns translation highlighted green
    print (f"{Back.GREEN}{translation}")
    translator_menu()