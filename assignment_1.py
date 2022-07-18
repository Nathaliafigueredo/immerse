import random

def load_words_list(file_name):
    ''' Function to load a text-file content in memory
    input: the name of a file containint the words
    output: a list containing all the words
    '''

def get_random_word(words_list):
    ''' Function to get a random word from a list of words
    input: a list of words
    output: one of the words in the list (random choice)
    '''

def get_masked_word(word):
    ''' Function to get a masked word from a word (drops ~50% of letters)
    input: the word as a string
    output: two things, the masked word (as a string) and a
      dictionary of masked words with their position in the word.
    '''
    #1. Define an empty dictionary for storing the dropped letters
    # This dictionary will use the letter as key, and a list of positions as value.
    # e.g. {"a": [1,3], "d": 2} means that the letter a is in position 1 and 3 in the word.
    
    #2. Iterate on the input word with a for-loop
    # Per each letter trow a coin (random number included in [0, 1], 50%)
    
    #3. If the random number is less than 0.5 keep the word,
    # if it is higher that 0.5 mask the letter and add its position in the dictionary.
    
    #4. When the for loop is finished return the masked word
    # and the dictionary of masked letters.


#0. Define a variable for the game score, e.g. score=3
# where 3 is the maximum number of attempts for guessing the word (score==0 the user lost)

#1. Load all the available words in memory (by reading them from a text file, or hard-coding them)
# You can encapsulate this piece of code in the function called load_words_list() above

#2. Pick a random word from all the available words.
# You can encapsulate this code into the function called get_random_word() above.

#3. Turn the letters in the word into capital letters, search for the default method .upper()

#4. Produce a masked version of the word (hide some letters).
# Write the code for the function get_masked_word().
# For example if the word is PENCIL the function get_masked_word() 
# returns something like P-N-I- or -EN-I- and a dictionary of the masked letters.
# The dictionary will use the masked letter as key, and a list of positions as value.
# e.g. {"a": [1,3], "d": 2} means that the letter "a" is in position 1 and 3 in the word.

#5. Print on screen the masked word and ask the user to 
# type a letter in the terminal, you can use the default method input()

#6. You need to check if the user provided more than one letter.
# Consider just the first character and discard the rest.

#7. Turn the character provided by the user into a capital letter

#8. Check if the letter provided by the user is a good one or a bad one.
# - First, check if the letter is already visible (the user did a mistake), decrease the score.
# - Second, if the letter is in the dictionary of masked letters, the user did a good choice 
#     (now you need to make those letters visible and remove the letter from the dictionary).
# - Third, the letter is neither in the visible letters, nor in the masked letters, decrease the score.

#9. Print the current user score, the masked word, and the list of letters already tried.
# If the score==0 the game is finished, a new match can start (score=3)
