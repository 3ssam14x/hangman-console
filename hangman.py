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
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #pass
    if len(letters_guessed) == 0: return False
    the_word = []
    for char in secret_word:
        if char not in the_word:
            the_word.append(char)
    for char in letters_guessed:
        if char not in secret_word or len(the_word) != len(letters_guessed): return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #pass
    word = list(secret_word)
    for i in range(len(word)):
        if word[i] not in letters_guessed:
            word[i] = "_ "
    return ''.join(word)

lower_case_chars = list(string.ascii_lowercase)

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #pass
    
    for char in letters_guessed:
        if char not in lower_case_chars: continue
        lower_case_chars.remove(char)
    return ''.join(lower_case_chars)
#letter_gussed = ['e', 'i', 'k' , 'p' , 'r' , 's']

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #pass
    print ("Welcome to the game Hangman!")
    print("I am thinking of a word that is {} letters long.".format(len(secret_word)))
    print("You have 3 warnings left.")
    print("--------------")
    print("You have 6 gussess left\nAvailabe letters: {}".format(string.ascii_lowercase))
    number_of_guesses = 6
    number_of_warnings = 3
    letters = []
    vowels = 'aeiou'
    wrong_guesses = []
    while True:
        lettter_guessed = input("Please guess a letter: ").lower()
        if str.isalpha(lettter_guessed) == False:
            number_of_warnings -= 1
            if number_of_warnings < 0: number_of_warnings = "no"
            # if number_of_warnings == 0:
            #     number_of_guesses -= 1
            print("Oops! That is not a valid letter. You have {} warnings left: {}".format(number_of_warnings, get_guessed_word(secret_word, letters)))
        else:
          if lettter_guessed in letters:
              number_of_warnings -= 1
              if number_of_warnings < 0:
                  print("Oops! You've already guessed that letter. You now have no warnings left")
              else:
                  print("Oops! You've already guessed that letter. You now have {} warnings left: {}".format(number_of_warnings , get_guessed_word(secret_word, letters)))
              # if number_of_warnings == 0:
              #     number_of_guesses -= 1
          else:
            if lettter_guessed in secret_word:
                letters.append(lettter_guessed)
                print("Good guess: {}".format(get_guessed_word(secret_word, letters)))
            else:
                if lettter_guessed in wrong_guesses:
                     number_of_warnings -= 1
                     if number_of_warnings < 0:
                        print("Oops! You've already guessed that letter. You now have no warnings left")
                     else:print("Oops! You've already guessed that letter. You now have {} warnings left: {}".format(number_of_warnings , get_guessed_word(secret_word, letters)))
                else:
                  if lettter_guessed in vowels:
                      number_of_guesses -= 2
                  else: number_of_guesses -= 1
                  if lettter_guessed not in letters:
                    wrong_guesses.append(lettter_guessed)
                    print("Oops! That letter is not in my word: {}".format(get_guessed_word(secret_word, letters)))
        if is_word_guessed(secret_word, letters) == True:
            print("----------------------\nCongratulations, you won\nYour total score for this game is: {}".format(number_of_guesses * len(letters)))
            break
        if number_of_warnings < 0:
            number_of_guesses -= 1
            print("so you lose one guess: {}".format(get_guessed_word(secret_word,letters)))
        if number_of_guesses == 0:
            print("Sorry, you ran out of guesses. The word was {}".format(secret_word))
            lower_case_chars = list(string.ascii_lowercase)
            break
        print("--------------")
        print("You have {} guesses left.".format(number_of_guesses))
        print("Availabe letters: {}".format(get_available_letters(letters + wrong_guesses)))

            





# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #pass
    my_word = my_word.strip().replace("_ ", "_")
    
    if len(my_word) != len(other_word): return False
    i = 0
    for i in range(len(my_word)):
        if my_word[i] == "_": continue
        if my_word[i] != other_word[i]: return False
    return True
#print(match_with_gaps("a_ ple", "apple"))

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #pass
    ans_words = []
    my_word = my_word.strip().replace("_ ", "_")
    for word in wordlist:
        if match_with_gaps(my_word, word): ans_words.append(word)
        else: continue
    if len(ans_words) > 0 :
        print(ans_words)
    else: print("No matches found")
                       

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains # cnt = 0
        # if len(word) != len(my_word): continue
        # for i in range(len(my_word)):
        #     if my_word[i] == "_" :
        #         cnt += 1
        #         continue
        #     elif word[i] != my_word[i]: break
        #     else: cnt += 1
        # if cnt == len(my_word): ans_words.append(word)and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      number_of_guesses > 0
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #pass
    print ("Welcome to the game Hangman!")
    print("I am thinking of a word that is {} letters long.".format(len(secret_word)))
    print("You have 3 warnings left.")
    print("--------------")
    print("You have 6 gussess left\nAvailabe letters: {}".format(string.ascii_lowercase))
    number_of_guesses = 6
    number_of_warnings = 3
    letters = []
    vowels = 'aeiou'
    wrong_guesses = []
    while True:
        lettter_guessed = input("Please guess a letter: ").lower()
        if (lettter_guessed == "*"):
            print("possible words matches are")
            show_possible_matches(get_guessed_word(secret_word, letters))
            continue
            #print("You have 6 gussess left\nAvailabe letters: {}".format(string.ascii_lowercase))
        if str.isalpha(lettter_guessed) == False:
            number_of_warnings -= 1
            if number_of_warnings < 0: number_of_warnings = "no"
            # if number_of_warnings == 0:
            #     number_of_guesses -= 1
            print("Oops! That is not a valid letter. You have {} warnings left: {}".format(number_of_warnings, get_guessed_word(secret_word, letters)))
        else:
          if lettter_guessed in letters:
              number_of_warnings -= 1
              if number_of_warnings < 0:
                  print("Oops! You've already guessed that letter. You now have no warnings left")
              else:
                  print("Oops! You've already guessed that letter. You now have {} warnings left: {}".format(number_of_warnings , get_guessed_word(secret_word, letters)))
              # if number_of_warnings == 0:
              #     number_of_guesses -= 1
          else:
            if lettter_guessed in secret_word:
                letters.append(lettter_guessed)
                print("Good guess: {}".format(get_guessed_word(secret_word, letters)))
            else:
                if lettter_guessed in wrong_guesses:
                     number_of_warnings -= 1
                     if number_of_warnings < 0:
                        print("Oops! You've already guessed that letter. You now have no warnings left")
                     else:print("Oops! You've already guessed that letter. You now have {} warnings left: {}".format(number_of_warnings , get_guessed_word(secret_word, letters)))
                else:
                  if lettter_guessed in vowels:
                      number_of_guesses -= 2
                  else: number_of_guesses -= 1
                  if lettter_guessed not in letters:
                    wrong_guesses.append(lettter_guessed)
                    print("Oops! That letter is not in my word: {}".format(get_guessed_word(secret_word, letters)))
        if is_word_guessed(secret_word, letters) == True:
            print("----------------------\nCongratulations, you won\nYour total score for this game is: {}".format(number_of_guesses * len(letters)))
            break
        if number_of_warnings < 0:
            number_of_guesses -= 1
            print("so you lose one guess: {}".format(get_guessed_word(secret_word,letters)))
        if number_of_guesses == 0:
            print("Sorry, you ran out of guesses. The word was {}".format(secret_word))
            lower_case_chars = list(string.ascii_lowercase)
            break
        print("--------------")
        print("You have {} guesses left.".format(number_of_guesses))
        print("Availabe letters: {}".format(get_available_letters(letters + wrong_guesses)))



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
   