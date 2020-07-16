
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    flag = True
    guess_dict = {}
    if word not in wordList:
        flag = False
    else:
        for letter in word:
            if guess_dict.get(letter,0) = 0
                guess_dict[letter] = 1
            else: 
                guess_dict += 1
            if letter not in hand:
                flag = False
                break
            elif hand[letter] < guess_dict.get(letter,0): 
                flag = False
                break
    return flag
