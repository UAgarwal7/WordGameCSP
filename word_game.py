""" a program that takes a phrase and either encodes it or decodes it
has a function that changes every letter to the one next to it
decodes does the opposite
parameters are the amount of spaces to move
"""


def coder(original_word, shift):



word = input("Enter the word: ")
word_list = list(word)
answer_with_count = {}
direction = input("Would you like this to be encoded or decoded?")
shift = input('How many places would you like the letters to be moved')
if direction == 'encoded':
    print('encoded')
elif direction == 'decoded':
    print('decoded')
else:
    print('Please enter the word encoded or decoded')

print('Thanks for playing!')
