# Problem A
def glorious(val):
    '''
    Purpose: To identify numbers not divisible by any number from
    10 to 50

    Parameter: A number

    Return value: Whether that number is 'glorious'
    '''
    glory = True
    for i in range(10,50):
        if val % i == 0:
            glory = False
    return glory

# Problem B
def count_glorious(low, high):
    '''
    Purpose: To identify the amount of glorious numbers in a
    given range

    Parameters: The starting and ending numbers of the range

    Return value: The amount of glorious numbers in the range
    '''
    g = 0
    if low > high:
        return 0
    for j in range(low, high + 1):
        glory = glorious(j)
        if glory == True:
            g += 1
        else:
            g += 0
    return g

# Problem C
def durdle_match(guess, target):
    '''
    Purpose: To allow players to make successive guesses at a word
    until they guess correctly

    Parameters: The player's guess and the target word

    Return value: A five letter string indicating which letters
    do not appear in the string, which letters appear in the
    string at another location, and which letters were guessed
    correctly.
    '''
    guess_check = ''
    Green = 'G'
    Blue = 'B'
    Yellow = 'Y'
    for i in range(5):
        if guess[i] == target[i]:
            guess_check += Green
        elif guess[i] in target:
            guess_check += Yellow
        else:
            guess_check += Blue
    return guess_check

# Problem D
def durdle_game(target):
    '''
    Purpose: To take a target to guess and prompt the user to
    guess until they find the word

    Parameter: The target word

    Return Values: A five letter string indicating which letters
    do not appear in the string, which letters appear in the
    string at another location, and which letters were guessed
    correctly; and the number of guesses it took the user at the
    end
    '''
    print('Welcome to Durdle!')
    tries = 0
    hint = ''
    while hint != 'GGGGG':
        guess = input('Enter a guess:')
        hint = durdle_match(guess, target)
        print(hint)
        tries += 1
    print('Congratulations, you got it in',tries,'guesses!')
    return tries
