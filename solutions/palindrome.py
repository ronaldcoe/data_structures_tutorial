'''
Author: Ronald Coello ©2022 ronaldcoello85@gmail.com
Program Description:
Promprt for a word, phrase, or number and check if is a palindrome
Purpose:
Practice with stacks
'''
import copy

print('-'*70)
print('Program to check if a word, phrase, or number is a palindrome')
print('-'*70)

# Function to format the string to remove spaces and punctuation
def format_string(characters):
    formated_string = []
    for character in characters:
        if character not in {' ', ',', '.','?','!'}:
            formated_string.append(character.lower())
    return formated_string

# Function to reversed the formated string
def reverse_string(formated_string):
    reversed_string = []
    for i in range(len(formated_string)):
        reversed_string.append(formated_string.pop())
    return reversed_string

# Function to compare the formated string
def is_palindrome(formated_string, reversed_string):
    if formated_string == reversed_string:
        return True
    else:
        return False

def main():

    # Prompt the user for a word, phrase, or number
    characters = input('\nWhat is the word, prhase, or number?: ')
    formated_string = format_string(characters)
    reversed_string = reverse_string(copy.deepcopy(formated_string))

    if is_palindrome(formated_string, reversed_string):
        print(characters, 'is a palindrome')
    else:
        print(characters, 'is not a palindrome')


main()



