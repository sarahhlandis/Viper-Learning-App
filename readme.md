# Viper: A Translator and Language Learning Terminal Application

### Sources Used:
- CSV docs populated via https://copylists.com/french/list-basic-french-words/#google_vignette

### [gitHub Repository](https://github.com/sarahhlandis/Terminal_Application)

### [Source Control](https://github.com/sarahhlandis/Terminal_Application/commits/main)

### [Project Management](https://trello.com/b/L4tvjr7Q/t1a3-terminal-application)

### Style Guide:
This terminal application was made in accordance with the PEP8 styleguide.
- It features appropriate indentation to enhance code readability as well as blank lines to separate code blocks.
- All the files in this project include detailed comments, in order for developers to better understand what is going on. This also fosters a better environment for devs to make future modifications, refactoring, and/or add features.
- UTF-8 default coding
- Follows proper naming conventions (snake_case format) with semantic and easy-to-follow function/variable naming.


### Application Features
1. Use of various user input throughout the program
- The app will require user input at various point throughout the app both in terms of navigating thru the application as well as responding to application prompts. 
- Upon opening the application, the user will be required to input which mode they wish to enter: Translation, Learning, or Quiz mode.
- Based on this choice, the application will then enter the chosen mode.
- The translation mode will simply allow the user to input their desired text, select which language they wish to translate to, and then translate accordingly.
- At any given input point, the user can type \home or \exit to either return to the main Viper menu or exit the program completely.

2. Learning Mode
- The learning mode will allow the user to learn specific words from their relevant course learning files (in CSV file format).
- The user will specify which language they wish to study from (i.e. if they wish to study from english words, they will have to input the french translations and vice versa).
- The user will have the opportunity to practice the words in a sort of flashcard style way, where a word will be displayed and the user will have to enter the translation. The user will be alotted 3 tries to correctly guess the word.
- Upon exiting this mode, the application will output which words the user needs to work on in terms of displaying incorrectly guessed words, as well as words they guessed correctly.

3. Quiz Mode
- The Quiz mode can be accessed at any time from either of the other two modes.
- Quiz mode offers the user the chance to practice the words they've learned with an added time component.
- The user can specify how long they wish to play using a built-in timer (in seconds). This timer runs simultaneosly with the quiz word generator, using a method called threading.
- This mode will randomly generate a word from the file that the user has chosen, and require them to correctly translate, with one guess per question.
- Upon finishing the quiz, the application will generate a quiz report file which the user can take a look at and review metrics from their quiz session.

To note: 
- All sections will be able to be accessed internally from any of the other modes.
- Translate mode requires internet connection


### Implementation Plan
- Feature 1: I plan to prioritize the user input functionality first and foremost, as this is integral to the application running smoothly. Feature 1 will also include the basic translation mode as well.
- Feature 2: I plan to focus on the learning mode once the main "interface" is complete. Once I have created the logic for gathering file information and transferring it into a nested list, I can reuse this for the quiz mode.
- Feature 3: The quiz mode will be implemented a step behind the learning mode as the logic required is similar to that of the learning mode. I also need to look into running a timer simulatenously to when the user "starts" the quiz. 

- If you wish to see a more detailed process of my implementation plan, please review the below images or check out my Trello board (link at top).

![Feature1](./docs/f1.png)
![Feature2](./docs/f2.png)
![Feature3](./docs/f3.png)

Changes along the way (as of Dec 13):
![Feature1](./docs/input.png)
![Feature2](./docs/learning.png)
![Feature3](./docs/quiz.png)

Changes along the way (as of Dec 15):
![Feature2](./docs/learning2.png)


#### Project Management
- I chose to use Trello to manage this project. Please see below images of the implementation plan (with dates) I intend to follow in terms of building out the features of the application.

![ImplementationPlan](./docs/implementation_plan.png)

Progress as of Sat Dec 10
    ![ImplementationPlan-Update](./docs/implementation_update1.png)

Progress as of Tues Dec 13
    ![ImplementationPlan-Update2](./docs/implementation_update2.png)

Progress as of Thurs Dec 15
    ![ImplementationPlan-Update3](./docs/implementation_update3.png)

Progress as of Friday Dec 16
    ![ImplementationPlan-Update4](./docs/implementation_update4.png)


### Installation Guide and Help Documentation
#### 1. Installation Guide
1. Git Clone
        - Ensure you have Python installed on your computer. 
        Run ```python3 --version``` to confirm. If you recieve a message back saying something along the lines of
        ```python3: command not found```
        - run ```python --version``` to be certain as you may have a different version. 
        * Make sure your python version begins with a 3.
        To download python, visit: [Python official website](https://www.python.org/downloads/)
        - Once you're set up with Python3, open Terminal and cd into your desired location on your computer.
        - Create a directory and initialize it to get ready for cloning a remote repository.
        Run ```git init``` to do this.
        - From within that directory, run 
        ```git clone git@github.com:sarahhlandis/Terminal_Application.git```
        - cd into the directory titled Terminal_Application-main
        - To setup all required dependencies and activate the virtual environment, run 
        ```bash setup.sh```
        - Once this is complete, you're welcome to run ```bash runscript.sh``` to enter into the Viper Learning Application

2. Download Zip from GitHub
- Ensure you have Python installed on your computer. 
    - Run ```python3 --version``` to confirm. 
    - If you recieve a message back saying something along the lines of ```python3: command not found```
        - run ```python --version``` to be certain as you may have a different version. 
    Make sure your python version begins with a 3.
    - To download python, visit: [Python official website](https://www.python.org/downloads/)
- Once you're set up with Python3, return to the [Viper Repository](https://github.com/sarahhlandis/Terminal_Application) and click the green < >Code button.
- Download the zip file to your computer and open it (a main directory will appear called Terminal_Application-main)
- Open Terminal and cd into the directory titled Terminal_Application-main
- To setup all required dependencies and activate the virtual environment, run 
```bash setup.sh```
- Once this is complete, you're welcome to run ```bash runscript.sh``` to enter into the Viper Learning Application

#### 2. Required Dependencies
    - The required dependencies can be found in the requirements.txt file, located at ```Terminal_Application-main/requirements.txt```. Please note, an internet connection is required to use the translator mode. 
    - Python3 as noted above

#### 3. Help Documentation:
- This app is meant to be used by anyone for their relevant foreign language learning.
1. Uploading your own files: 
- To enable this app to suit your language requirements, please add your CSV files to the CSV folder:
    ```Terminal_Application-main/src/csv```
This is where you are able to store your own language learning files in order to populate the personalized quiz and learning module within the application.
    - When adding your own CSV files, please ensure you have a header row, with two columns: English and the language of your choosing. Please be sure the first column is English and the second is the foreign language.
        - This will ensure that the application can read your files accurately as the code is built around this stylistic formatting.
    - Also note, you can create these files in excel and then export them as required into CSV format. ** The application is compatible with CSV files only.
2. Character sensitivity:
- Being that Viper is a language learning application designed to help you learn new words, your responses are character-sensitive. This means that if you spell the word correctly, but neglect the proper accenting, the word will be marked wrong. (e.g. february = février, not fevrier)
** Please be sure you utilize appropriate accenting if your intended learning language includes special characters.
- To apply special characters, you can:
    1. Download the relevant language keyboard 
    2. Memorize your keyboard's deadkeys - this may not be as handy specifically within the quiz section, as there is a time component included.
    ** Please see the below relevant documentation for methods on how to type accented keys:
        - [Mac users](https://support.apple.com/en-au/guide/mac-help/mh27474/mac)
        - [Windows users](https://nerdschalk.com/how-to-type-accents-on-windows/)

#### 4. Application Development Testing
- Unit testing was conducted throughout the application's development on various features.
- If you wish to view the outcome of some of the documented unit testing, please refer to ```Terminal_Application-main/docs/app_testing``` where you can view the outcomes of the process.
For your convenience, you may also view it's findings here:
![Testing](ManualTesting.pdf)





