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
answer_word = input("Enter the word to be guessed: ")
answer_list = list(answer_word)
# insert code to search for duplicate here
current_guessed_letters = {}

game_end = False
while not game_end:
    guessed_word = input("Guess a word: ")
    guessed_list = list(guessed_word)
    for x in range (0,len(guessed_list)):
        current_letter: guessed_list[x]
        try:
            answer_index = answer_list.index(current_letter)
        except:
            break
        else:
            current_guessed_letters[current_letter] = answer_index - x
            # gives the differences of the indexes of the letter in the guessed word and the answer
        print(current_guessed_letters)