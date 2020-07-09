def no_dups(s):
    # make a answer variable to store words that are no duplicates
    answer = []
    # making a list of words aka (split)
    words = s.lower().split(' ')
    # ["spam", "cat", "spam"]
    # making a dictionary from a list using fromkeys and passing in our list (this should remove dupes)
    dictionary = dict.fromkeys(words)
    print(dict.fromkeys(words))
    # we now have a dictionary of the words without any duplicates in them
    for key in dictionary.keys():
        # for every key(aka word) in the dictionary
        answer.append(key)
        # append the key(aka word) to our answer array that is empty to begin with
        # adds spaced back into the answer
    return ' '.join(answer)

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))