# Warmup:
# river = "mississippi"
# print(river.count("s"))
# riverox = river.replace("iss", "ox")
# print(riverox)
# print(river.find("p"))

def foo(istring):
    p ='0123456789'
    os = ''
    for i in range(len(istring)):
        if istring[i] not in p:
            os += istring[i]
    return os

# Stretch:
def repeat_letters():

    word = input("Enter a word: ")
    word_list = []
    while word != '':
        first = word[0]
        if first in word[1:]:
            word_list.append(word)

        word = input("Enter a word: ")

    print(word_list)

def is_palindrome(pal):
    newpal = ''
    for ch in pal:
        if ch.isalpha():
            newpal += ch
    newpal = newpal.lower()
    if newpal == newpal[-1::-1]:
        return True
    else:
        return False

# Workout:
def igpay(word):
    vowel_index = 0
    consonants = ''
    while word[vowel_index] not in "aeiou":
        consonants += word[vowel_index]
        vowel_index += 1

    if vowel_index != 0:
         pig_latin = word[vowel_index:] + consonants + "ay"
    else:
        pig_latin = word + "way"
    return pig_latin

# Challenge:
def mysplit(stringarg, delimiter):
    split = []
    d1 = 0
    for i in range(stringarg.count(delimiter)+1):
        d2 = stringarg.find(delimiter, d1)
        if d2 == -1:
            d2 = len(stringarg)
        split.append(stringarg[d1:d2])
        d1 = d2+len(delimiter)
    return split




    # for i in range(len(stringarg)):
    #     if stringarg[i] == delimiter:
    #         stringarg[0:i]
    #
