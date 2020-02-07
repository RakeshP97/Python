# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
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



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string (of lowercase English letters), the word the user 
    is guessing;
    letters_guessed: list (of lowercase English letters), set of letters 
    that have been guessed so far;
    returns: bool, True if all the letters of secret_word are in 
    letters_guessed, and False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for ch in letters_guessed:
        if ch in secret_word:
            continue
        else:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string (of lowercase English letters), the word the user 
    is guessing;
    letters_guessed: list (of lowercase English letters), set of letters 
    that have been guessed so far;
    returns: string, a sequence of lowercase letters, and '_ ' (underscore
    followed by a single space) representing a partially guessed secret
    word. 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    newStr = ''
    for ch in secret_word:
        if ch in letters_guessed:
            newStr = newStr + ch
        else:
            newStr= newStr + '_ '
    return newStr


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of lowercase English letters), set of letters 
    that have been guessed so far;
    returns: string, a set of lowecase letters which have not 
    yet been guessed in alphabetical order.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    s = string.ascii_lowercase[:26]
    for ch in letters_guessed:
        s = s.replace(ch,'')
    return s
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Plays an interactive game of Hangman according to the rules
    defined in the assignment brief.
    
    Returns: tuple of boolean, integer, and string; 
    (True, number of remaining guesses, string of 
    lowecase letters still available) if
    the secret word was guessed;
    (False, number of remaining guesses, string of lowercase 
    letters still available) if
    the secret word was not guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print('Welcome to the game Hangman!')
    l = len(secret_word)
    print('I am thinking of a word that is {0} letters long.'.format(l))
    no_guess = 6
    letters_guessed = [];
    while no_guess > 0:
        print('----------------------------------------')
        print('You have {0} guess left.'.format(no_guess))
        print('Available letters: {0} \n'.format(get_available_letters(letters_guessed)))
        ch_guess = input('Please guess a letter: ')
        if ch_guess in letters_guessed:
            print("Oops! You've already guessed that letter: {0}".format(get_guessed_word(secret_word,letters_guessed)))
        else:
            letters_guessed.append(ch_guess)
            if ch_guess in secret_word:
                print('Goodguess: {0}'.format(get_guessed_word(secret_word,letters_guessed)))
                if get_guessed_word(secret_word,letters_guessed).lower() == secret_word.lower():
                    print('Congratulations, you won!')
                    return [True, no_guess, get_guessed_word(secret_word,letters_guessed)];
            else:
                print('Oops! That letter is not in my word: {0}'.format(get_guessed_word(secret_word,letters_guessed)))
                no_guess = no_guess -1;
    print('Reached max number of guess')
    return [False, no_guess, get_guessed_word(secret_word,letters_guessed)];




# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)

if __name__ == "__main__":

    # To test your impelementation, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)