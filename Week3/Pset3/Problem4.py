# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string
WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    flag = True
    for letter in secretWord:
        if letter not in lettersGuessed:
            flag = False
    return flag



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    out = []
    ls_string = list(secretWord)
    for i in range(len(ls_string)):
        if ls_string[i] in lettersGuessed:
            out.append(ls_string[i])
        else:
            out.append('_ ')
    return(''.join(out))



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    available_letters = string.ascii_lowercase
    for letter in lettersGuessed:
        available_letters = available_letters.replace(letter,'')
    return available_letters

    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print('Welcome to the game, Hangman!')
    print('I am thinking of word that is ' + str(len(secretWord)) + ' letters long.')
    print('-----------')
    attempts = 8
    available_letters = []
    lettersGuessed =[]
    while True:

        if isWordGuessed(secretWord, lettersGuessed):
            print('Congratulations, you won')
            break
        elif attempts == 0:
            print("Sorry, you ran out of guesses. The word was else.")
            break
        else: 
            print('You have ' + str(attempts) + ' guesses left.')
            available_letters = getAvailableLetters(lettersGuessed)
            print('Available letters : ' + available_letters)
            guessed_word = input('Please guess a letter:')           
            guess_lower_case =  guessed_word.lower()
            if len(guessed_word)>1:
                print('Ops, please guess just one letter')
            elif (guess_lower_case in lettersGuessed):
                words_guessed = getGuessedWord(secretWord, lettersGuessed)
                print("Oops! You've already guessed that letter: "+ words_guessed)
                print('-----------')
            elif (guess_lower_case not in secretWord):
                attempts -= 1
                lettersGuessed.append(guess_lower_case)
                words_guessed = getGuessedWord(secretWord, lettersGuessed)
                print("Oops! That letter is not in my word: "+ words_guessed)
                print('-----------')
            else:
                lettersGuessed.append(guess_lower_case)
                words_guessed = getGuessedWord(secretWord, lettersGuessed)
                print('Good guess: ' + words_guessed)
                print('-----------')







# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
