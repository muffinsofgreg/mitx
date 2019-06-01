# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import os
import time
import random

WORDLIST_FILENAME = "words.txt"


def play_loop(game):

    yes = ['Y', 'y', 'yes']
    play_again = True

    while play_again is True:
        game()
        if input("\nPlay Again? ") not in yes:
            play_again = False


def display_title():
    os.system('clear')

    print("\t***********************************")
    print("\t**********  Hangman  **************")
    print("\t***********************************")
    print('-------------------------------------------------')
    print('\n')
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ', len(secretWord), 'letters long.')
    print('\n')


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")

    with open(WORDLIST_FILENAME, 'r') as inFile:
        time.sleep(1)
        # line: string
        line = inFile.readline()
        # wordlist: list of strings
        wordlist = line.split()

    print("  ", len(wordlist), "words loaded.")
    time.sleep(1)

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
    wordGuessed = True
    for letter in secretWord:
        if letter not in lettersGuessed:
            wordGuessed = False
            break
    return wordGuessed


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''

    hiddenWord = ""
    for letter in secretWord:
        if letter in lettersGuessed:
            hiddenWord += letter + ' '
        else:
            hiddenWord += '_ '
    return hiddenWord


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    newAlphabet = ""

    for letter in alphabet:
        if letter not in lettersGuessed:
            newAlphabet += letter

    return newAlphabet


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
    guessesLeft = 3
    lettersGuessed = []

    def display_guess_status():
        print(getGuessedWord(secretWord, lettersGuessed))
        print('\n')
        print('You have {} guesses left.'.format(guessesLeft))
        print('Available Letters: {}'.format(
              getAvailableLetters(lettersGuessed)))
        print('\n')

    while guessesLeft > 0 and isWordGuessed(secretWord, lettersGuessed) is False:

        display_title()
        display_guess_status()

        guess = str(input('Please guess a letter: ')).lower()

        if guess in lettersGuessed:
            print("Oops! You've already guessed that Letter!")
            time.sleep(1.5)

        elif guess not in secretWord:
            lettersGuessed.append(guess)
            guessesLeft -= 1
            print("Oops! That letter is not in my word!")
            time.sleep(1.5)

        else:
            lettersGuessed.append(guess)
            print("Good guess!")
            time.sleep(1.5)

    if isWordGuessed(secretWord, lettersGuessed) is True:
        display_title()
        display_guess_status()
        print('----------')
        print('Congratulations, you won!')

    else:
        print('----------')
        print('Sorry, you ran out of guesses. The word was {}.'.format(secretWord))

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)


if __name__ == "__main__":
    # secretWord = chooseWord(wordlist).lower()
    secretWord = 'bongle'
    game = hangman(secretWord)
    play_loop(game)
