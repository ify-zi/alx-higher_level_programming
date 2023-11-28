#!/usr/bin/python3
def islower(letter):
    checker = ord(letter)
    if checker >= 97 and checker <= 122:
        return True
    else:
        return False
