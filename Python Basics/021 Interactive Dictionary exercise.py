'''
Write a program that implements a simple interactive dictionary. Start by prompting the user with the following:

Enter a word in English or EXIT: << put a space at the end of this message

When the user enters EXIT in capital letters, terminate the program with the following:

Bye!

Otherwise, try to find the German equivalent in the dictionary provided in the exercise.

a. if the word is in the dictionary, print: Translation: {} << replace {} with the word from the dictionary
b. if the word is not in the dictionary, print: No match!

You should keep asking the user for new words with the same prompt ('Enter a word in English or EXIT: ') until the user provides EXIT.

Here's an example of how the program could work with user input shown in the bold:

Enter a word in English or EXIT: dog
No match!
Enter a word in English or EXIT: face
Translation: Gesicht
Enter a word in English or EXIT: EXIT
Bye!'''

sample_dict = {
    "mouth": "Mund",
    "finger": "Finger",
    "leg": "Bein",
    "hand": "Hand",
    "face": "Gesicht",
    "nose": "Nase"
}
while True:
    word = input('Enter a word in English or EXIT: ')
    if word == 'EXIT':
        print('Bye!')
        break
    elif word in sample_dict:
        print('Translation:', sample_dict[word])
    else:
        print("No match!")