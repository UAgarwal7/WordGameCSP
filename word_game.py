""" a word game that has one user enter a word and the other try and guess it. Any number of letters. number will not be known to guesser guesser guesses words (no repeats)

start of the game: guesser receives info about # of duplicate letters and how many times they appear
receives hint about word length
also gets relative position of letters -- first time guesser guesses a correct letter in the wrong spot, they will be told which direction a letter is in
-- second+ time, they will be told the direction, and the letter -- correct letters will be known
 If word is correct, game ends, keep track of score
Variables: str word input
list word letters
list word letter guesses (keeps track of how many times each letter was guessed)
list correct letters
guess count

things to make a guess work (put in function): function guess (parameter is word to guess) returns dictionary: key is letter
str guessed word
list guessed word letters

word processing at the beginning:
    input answer word
    make into list with each letter
    search for duplicates
        get to later - lower priority

    input guessed word
    make each letter of the guessed word an element of a list guessed word
function guess (word to guess list, guessed list)
    for loop going through the indexes of the guessed word list (iteration)
        use the find function in a try-except for each letter in the guessed string to get the index
        if it is successful, add the letter and the index to a dictionary (selection)
    Once the entire guessed word has been gone through, return the dictionary

Edge cases to test:
    duplicate letters in answer
    duplicate letters in guess
"""


def guess(answer_list, guess_list):
    current_guessed_letters = {}
    for x in range(0, len(guess_list)):
        current_letter = guess_list[x]
        try:
            answer_index = answer_list.index(current_letter)
        except:
            break
        else:
            current_guessed_letters.update({current_letter: str(answer_index - x)})
            # gives the differences of the indexes of the letter in the guessed word and the answer
        # print(current_guessed_letters)
    return current_guessed_letters


answer_word = input("Enter the word to be guessed: ")
answer_list = list(answer_word)
# insert code to search for duplicate here
answer_with_count = {}
for x in range(len(answer_list)):
    answer_with_count.update({answer_list[x]: 0})
    print(answer_with_count)
game_end = False
print('The word has ' + str(len(answer_word)) + ' letters.')
print('Note: All hints refer to the last instance of the letter in the guess.')
print('Example: The word hello told you that the letter l is 2 positions ahead in the answer.')
print('This refers to the second l, so the letter l is at the 6th position in the answer.')
while not game_end:
    guessed_word = input("Guess a word: ")
    guessed_list = list(guessed_word)
    current_guessed_letters = guess(answer_list, guessed_list)
    # I have a dictionary that has each correct letter and its relative position to the answer
    # I need to display this to the player
    if guessed_word == answer_word:
        game_end = True
    else:
        for x in current_guessed_letters:
            answer_with_count[x] += 1
            # take the value x and look for its value in the other list to
            if answer_with_count[x] >= 2:
                print("The letter " + str(x) + " is " + current_guessed_letters[x] + " position(s) ahead in the answer")
            elif answer_with_count[x] == 1:
                print("A letter you guessed is " + current_guessed_letters[x] + " position(s) ahead in the answer")

print('Thanks for playing!')
