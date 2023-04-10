""" a word game that has one user enter a word and the other try and guess it. Any number of letters. number will not be known to guesser guesser guesses words (no repeats)

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

function guess (word to guess)
    input guessed word
    make each letter of the guessed word an element of a list guessed word
    for loop going through the indexes of the guessed word list
        use the find function in a try-except for each letter in the guessed string to get the index
        if it is successful, add the letter and the index to a dictionary
"""