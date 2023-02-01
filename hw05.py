# Problem A.
def closest(vals):
    '''
    Purpose: to take a list of integers and return the smallest difference
    between any pair

    Parameter: a list of integers

    Return value: an integer representing the smallest difference found
    '''
    diffs = []
    for i in range(len(vals)):
        for j in range(len(vals)):
            dif = abs(vals[i]-vals[j])
            if dif != 0:
                diffs.append(dif)
        min = diffs[0]
        for num in diffs:
            if num < min:
                min = num
    return min

# Problem B.
def change_key(notes, up):
    '''
    Purpose: to move a given amount of musical notes up or down the
    scale a given amount of steps

    Parameters: a list of musical notes and the amount of steps to move them

    Return Value: a new list of musical notes
    '''
    scale = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    scale_to_num = [1,2,3,4,5,6,7,8,9,10,11,12]
    new_scale = []
    for j in notes:
        new_scale += [scale[scale_to_num[(scale_to_num[scale.index(j) - 1] + up) % 12] - 1]]
    return new_scale

#Problem C.
def avoid_sz(names_list):
    '''
    Purpose: to reorder a list of names so that no names with an 's' or a 'z'
    are in even positions

    Parameter: a list of names

    Return Value: a new list with only valid names in the even positions
    '''

    valid_list = []
    invalid_names = []
    valid_names = []
    for i in names_list:
        if ('S' in i or 'Z' in i or 'z' in i or 's' in i) is True:
            invalid_names.append(i)
        else:
            valid_names.append(i)
    rest_of_valid = valid_names[:]
    if len(invalid_names) > len(valid_names):
        print("Impossible: Too many s/z names")
        return valid_list
    for j in range(len(invalid_names)):
        valid_list.append(valid_names[j])
        valid_list.append(invalid_names[j])
        rest_of_valid.pop(0)
    valid_list = valid_list + rest_of_valid
    return valid_list
