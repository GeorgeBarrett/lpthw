def break_words(stuff):
    # .split() makes the string intot a list
    words = stuff.split(' ')
    return words

def sort_words(words):
    # sorts the words
    return sorted(words)

def print_first_word(words):
    # .pop(0) pops off the first word
    # word is a new variable that stores the first word from words
    word = words.pop(0)
    print(word)

def print_last_word(words):
    # .pop(-1) pops off the last word
    # same logic as function above 
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    # takes in a full sentence and returns the sorted words
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    # this prints the first and last word of the sentence
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sentence_sorted(sentence):
    # sorts the words and then prints the first and last one
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)