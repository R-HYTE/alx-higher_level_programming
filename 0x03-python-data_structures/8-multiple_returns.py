#!/usr/bin/python3
def multiple_returns(sentence):
    # Get the length of the sentence
    length = len(sentence)

    if length == 0:
        first_char = None
    else:
        # Get the first character of the sentence
        first_char = sentence[0]

    return (length, first_char)
