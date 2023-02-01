# Problem A.
def collatz(n):
    '''
    Purpose: to run the collatz conjecture for an integer n and count how
    many elements are in the sequence
    Parameter(s): an integer n
    Return Value: the amount of elements in the collatz sequence
    '''
    if n == 1:
        return 1
    elif n % 2 == 0:
        return collatz(n//2) + 1
    elif n % 2 != 0:
        return collatz(3 * n + 1) + 1

# Problem B.
def is_target(lines):
    '''
    Purpose: To check if a list of strings has an 'A', 'C', 'M', or 'E' in every
    string
    Parameter(s): A list of strings
    Return Value: True if the file is a target, false if it's a decoy
    '''
    if lines == []:
        return True
    elif ('A' not in lines[0] and 'C' not in lines[0] and 'M' not in lines[0]
    and 'E' not in lines[0]):
        return False
    else:
        return is_target(lines[1:])

# Problem C.
    '''
    Purpose: To print a list of the paths to all the files that are targets
    Parameter(s): Some file path to the top-level directory
    Return Value: A list of the paths to all the files that are targets
    '''
import os
def all_targets(path):
    targets = []
    for file in os.listdir(path):
        if os.path.isfile(path+'/'+file):
            document = open(path+'/'+file)
            docu_list = document.readlines()
            if is_target(docu_list) is True:
                targets += [path+'/'+file]
            document.close()
        else:
            targets += all_targets(path+'/'+file)
    return targets
