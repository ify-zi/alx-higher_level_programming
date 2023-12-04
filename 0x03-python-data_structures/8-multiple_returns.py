#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        first_letter = None
        length = 0
    else:
        length = len(sentence)
        first_letter = sentence[0]

    return (length, first_letter)
