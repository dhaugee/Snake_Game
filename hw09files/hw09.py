import math
import random

# Problem A.
def cookie_order(dictionary):
    '''
    Purpose: To take in cookie typse and numbers of cookies desired and return
    the cookies with the number of boxes per cookie needed for them to be purchased
    Parameter(s): A dictionary with the cookie types as keys and amount of cookies
    desired as values
    Return Value: A dictionary with the cookie types as keys and amount of boxes
    needed as values
    '''
    for k in dictionary:
        dictionary[k] = (math.ceil(dictionary[k] / 30))
    return dictionary

# Problem B.
def follow_words(text):
    '''
    Purpose: To create a dictionary where each key will be a word from the
    text string, and each value will be a list of all of the words that directly
    follow that word.
    Parameter(s): A string
    Return Value: A dictionary where each key will be a word from the text
    string, and each value will be a list of all of the words that directly
    follow that word.
    '''
    text_list = text.split(' ')
    keys = []
    values_list = []
    new_dict = {}
    for i in range(len(text_list)):
        if text_list[i] not in keys:
            try:
                values = [text_list[i+1]]
                keys.append(text_list[i])
                values_list.append(values)
            except IndexError:
                for j in range(len(keys)):
                    new_dict.update({keys[j]: values_list[j]})
                return new_dict
        elif text_list[i] in keys:
            try:
                values = values_list[keys.index(text_list[i])]
                new_values = text_list[i+1]
                values.append(new_values)
                values_list[keys.index(text_list[i])] = values
            except IndexError:
                for j in range(len(keys)):
                    new_dict.update({keys[j]: values_list[j]})
                return new_dict

# Problem C.
def auto_complete(follows_dict, current):
    '''
    Purpose: To take the dictionary returned in follow_words(text) and a word,
    and suggest autocompletions for it based off the text the dictionary is
    based off of
    Parameter(s): A dictionary from follow_word(text) and a single world
    Return Value: A list of autocompletions for the word based off the text the
    dictionary is based off of
    '''
    all_keys = []
    for word in follows_dict.keys():
        all_keys.append(word)
    suggestions = follows_dict.get(current, all_keys)
    return suggestions

# Problem D.
def random_sent(fname, max_length):
    '''
    Purpose: To take a text file and sentence length and randomly generate a
    sentence from it
    Parameter(s): A text file and integer containing a sentence length
    Return Value: A randomly generated sentence
    '''
    text_file = open(fname)
    text = text_file.read()
    text = text.replace('\n', ' ')
    valid_dict = follow_words(text)
    word_list = text.split(' ')
    current = random.choice(word_list)
    sentence_list = [current]
    sentence = ''
    for word in sentence_list:
        if '.' in word or '!' in word or '?' in word:
            for i in range(len(sentence_list)):
                sentence += sentence_list[i] + ' '
            return sentence
        if len(sentence_list) == max_length:
            for j in range(len(sentence_list)):
                sentence += sentence_list[j] + ' '
            return sentence
        sentence_list.append(random.choice(auto_complete(valid_dict, word)))








    # sentence_words = [str(random.choice(list(valid_dict)))]
    # sentence = ''
    # for word in sentence_words:
    #     sentence_words.append(random.choice(auto_complete(valid_dict, word)))
    #     if '.' or '!' or '?' in word or len(sentence_words) == max_length:
    #         for word in sentence_words:
    #             sentence = sentence + word + ' '
    #             return sentence
