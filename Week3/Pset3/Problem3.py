"""
Next, implement the function getAvailableLetters that takes in one parameter 
-a list of letters, lettersGuessed. This function returns a string that is comprised 
of lowercase English letters - all lowercase English letters that are not in lettersGuessed.

Example Usage:

lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getAvailableLetters(lettersGuessed))
abcdfghjlmnoqtuvwxyz
"""
import string


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    available_letters = string.ascii_lowercase
    for letter in lettersGuessed:
        available_letters = available_letters.replace(letter,'')
    return available_letters

