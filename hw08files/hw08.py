import random

# Problem A
def get_word_list(filename):
    '''
    Purpose: To take in a text file containing acceptable
    Durdle words and return a list of the words
    Parameter: A text file
    Return Value: A list of Durdle words
    '''
    file = open(filename)
    durdle_list = file.readlines()
    for i in range(len(durdle_list)):
        if '\n' in durdle_list[i]:
            durdle_list[i] = durdle_list[i][:len(durdle_list[i])-1]
    return durdle_list

# Problem B
def durdle_match(guess, target):
    '''
    Purpose:
        Determines which letters in the user's guess match the target
    Parameters:
        guess - a 5-letter string representing the user's guess
        target - a 5-letter string representing the target word
    Return Value:
        A 5-letter string, where each letter represents whether or not
        the letter in that position is correct.  'B' means the letter
        is not present in the target, 'Y' means that it's present in
        a different location, 'G' means it's in the correct location.
    '''
    matches = ''
    for i in range(5):
        if guess[i] not in target:
            matches += 'B'
        elif guess[i] == target[i]:
            matches += 'G'
        else:
            matches += 'Y'
    return matches

def durdle_game():
    '''
    Purpose: Lets the user play a game where they try to match
    a target word
    Parameters: None
    Return Value: The number of guesses it took the user to
    get the correct word.
    '''
    print("Welcome to Durdle!")
    durdle_list = get_word_list('words_full.txt')
    guess = ''
    count = 0
    target = random.choice(durdle_list)
    while guess != target:
        guess = input("Enter a guess:")
        if guess in durdle_list:
            print('              '+durdle_match(guess, target))
            count += 1
        if guess not in durdle_list:
            print('Not in our vocab or wrong length, give it another shot')
    print("Congratulations, you got it in",count,"guesses!")
    return count

# Problem C
def grade_quiz(file_name):
    '''
    Purpose: To return the scores of three question on a
    quiz
    Parameter: A file containing the answers to the three questions
    Return Value: The scores to each question
    '''
    try:
        file = open(file_name)
        answers = file.readlines()
        points = []
        for i in range(len(answers)):
            if '\n' in answers[i]:
                answers[i] = answers[i][:len(answers[i])-1]
        try:
            if answers[0] == '42':
                points.append(2)
            elif answers[0] == '':
                points.append(0)
            else:
                points.append(1)
        except IndexError:
            points.append(0)
        try:
            if answers[1] == 'Belgium':
                points.append(2)
            elif answers[1] == '':
                points.append(0)
            else:
                points.append(1)
        except IndexError:
            points.append(0)
        try:
            if answers[2] == 'Towel':
                points.append(2)
            elif answers[2] == '':
                points.append(0)
            else:
                points.append(1)
        except IndexError:
            points.append(0)
        return points
    except FileNotFoundError:
        return [0,0,0]

# Problem D
def grade_all(grade_file):
    '''
    Purpose: to take a CSV file with all students' names and
    create a CSV file with all students and their scores for
    each question
    Parameter: a gradebook file
    Return Value: a CSV file with all students and their scores
    for each question
    '''
    blank = open(grade_file, 'r')
    filled = open('updated_' + grade_file, 'w')
    i = 1
    for row in blank:
        if i == 1:
            filled.write('First Name,Last Name,Q1 Grade,Q2 Grade,Q3 Grade\n')
            i += 1
        else:
            access = row.split(',')
            student_file_name = access[0].lower() + '_' + access[1].lower() + '.txt'
            Qu1 = str(grade_quiz(student_file_name)[0])
            Qu2 = str(grade_quiz(student_file_name)[1])
            Qu3 = str(grade_quiz(student_file_name)[2])
            filled.write(access[0] + ',' + access[1] + ',' + Qu1 + ',' + Qu2 + ',' + Qu3 + '\n')
