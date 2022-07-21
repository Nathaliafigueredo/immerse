import random

def get_masked_word(word):
    ''' Function to get a masked word from a word (drops ~50% of letters)
    e.g. "CAVIAR" -> "C-V--R"; "UNICORN" -> "U-IC-R-"
    input: the word as a string
    output: the masked word (as a string) and a
      dictionary of masked letters with their position in the word.
    Example: get_masked_word("UNICORN") can return the tuple
    ('U-IC---', {'N': [1, 6], 'O': [4], 'R': [5]})
    '''
    # Get unique letters in the word
    unique_letters_list = list(set(word)) # set() finds unique elements in string
    # Shuffling the list of unique letters
    random.shuffle(unique_letters_list)
    # Selecting just 50% of the letters
    split_point = len(unique_letters_list) // 2
    letters_to_mask_list = unique_letters_list[0:split_point]
    # Creating the masked word and the dictionary
    masked_word = ""
    masked_letter_position_dict = {}
    for letter_position, letter in enumerate(word):
        if(letter in letters_to_mask_list):
            masked_word = masked_word + "-"
            # We store the position of the masked letter in a dictionary
            if(letter in masked_letter_position_dict):
                # If the letter is in the dictionary we append the position
                masked_letter_position_dict[letter].append(letter_position)
            else:
                # If the letter is NOT in the dictionary we create the entry (a list)
                masked_letter_position_dict[letter] = [letter_position]
        else:
            masked_word = masked_word + letter        
    # Finished, let's return the masked letters and the
    # dictionary containinng the position of the masked letters.
    return masked_word, masked_letter_position_dict


#0. Define a variable for the game score, e.g. score=3
# where 3 is the maximum number of attempts for guessing the word (score==0 the user lost)

#1. Load all the available words in memory (by reading them from a text file, or hard-coding them)

#2. Pick a random word from all the available words.

#3. Turn the letters in the word into capital letters, search for the default method .upper()

#4. Use the function get_masked_word() that I provided for you above.
# This function returns the masked word, and a dictionary.
# The dictionary contains the masked letters as keys,
# and a list of their positions as values.
# e.g. if you call the function in this way: get_masked_word("UNICORN")
# the result could be: ('U-IC---', {'N': [1, 6], 'O': [4], 'R': [5]})

#5. Print on screen the masked word and ask the user to 
# type a letter in the terminal, you can use the default method input()

#6. You need to check if the user provided more than one letter.
# If this is the case, take just the first character and discard the rest.

#7. Turn the character provided by the user into a capital letter

#8. Check if the letter provided by the user is a good one or a bad one.
# Recall: in step-4 you used the function get_masked_word() to get a dictionary of masked letters.
# If the letter is in the dictionary then it's a GOOD one (show this letter in masked_word)
# If the letter is NOT in the dictionary it's a BAD one (decrease the score)

#9. Print the current user score, the masked word, and the list of letters already tried.
# If the score==0 the game is finished, a new match can start (set again score=3)
