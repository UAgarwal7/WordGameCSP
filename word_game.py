import random

"""
Program Description:
This program allows the user to input any phrase less than 10 characters long and get it encrypted.

The encrypting algorithm randomizes the order of the letters in the word.
The decrypting algorithm can undo the randomization given the coded word and a key (which is provided after encryption)
"""


"""
This function turns a list of characters into a string. It does this by iterating through the string and adding all of the
characters to a new string that it creates
"""
def list_to_string(letters):
    return_string = ''
    for x in letters:
        return_string += str(x)

    return return_string


"""
This function takes a word and a key and applies a permutation cipher algorithm to change the word.
    Depending on how it is called, the function will decide whether to encode or decode.

Inputs:
    word_list: The word that will be changed
    key: a list of numbers that have the indexes that each letter in each group will shift.
        Example: The key 2,0,3,1 indicates that the letter in the 1st index in the original group will be at the end of the
            new group. This key would scramble the group 'abcd' into 'cadb'

Outputs:
    returns the changed word
"""
def word_processing(word_list, key_list):
    final_list = []
    if key_list[-1] != -1:
        # Encoding sequence
        for x in range(len(key_list)):
            new_index = key_list[x]
            final_list.append(word_list[new_index])
    elif key_list[-1] == -1:
        # Decoding sequence
        for x in range (len(key_list)-1):
            letter_index = key_list.index(x)
            final_list.append(word_list[letter_index])
    return final_list


user_input = input('What do you want to do? e - encipher a word, d - decipher a word: ')
if user_input == 'e':
    word = input('Please enter the phrase to be encoded (must be less than 10 characters): ')
    word_list = list(word)
    if len(word_list) >= 10:
        print("Please rerun the program and enter a word with less than 10 characters")
        quit()

    key_list = []
    for x in range(len(word)):
        key_list.append(x)

    random.shuffle(key_list)
    return_key = ''
    print('The coded word is: ' + list_to_string(word_processing(word_list, key_list)))
    print('The key to decode is: ' + list_to_string(key_list))

elif user_input == 'd':
    coded_word = input('Please enter the word to be decoded: ')
    key = list(input('Please enter the key: '))
    for x in range(len(key)):
        key[x] = int(key[x])
    key.append(-1)
    print("The decoded word is: " + list_to_string(word_processing(coded_word, key)))

else:
    print('The value you entered is not an option, please restart the program to try again.')
