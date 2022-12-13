# TRANSLATOR MODE

import googletrans
import textblob
from functions.translator_menu import translator_menu

# Get languages from googletrans pkg dictionary
languages=googletrans.LANGUAGES

# Create a list from googletrans dict with values only
language_list=list(languages.values())

# Function for translator
def translator():
    #Translate mode entry message
    print('''You're now in Viper Translate Mode. Please follow the below
        prompts to translate - \n''')

    # Get user input for original language
    original_lang=input("Origin language: ").lower()
    for key, value in languages.items():
        if (value==original_lang):
            original_key=key

    # Get user input for desired language
    desired_lang=input("Desired language: ").lower()
    for key, value in languages.items():
        if (value==desired_lang):
            desired_key=key

    # Get user input that determines phrase they wish to translate
    sentence=input("Enter phrase: ")
    words=textblob.TextBlob(sentence)

    # Translates user text
    translation=words.translate(from_lang=original_key,to=desired_key)
    print (f"\n{translation}")
    translator_menu()