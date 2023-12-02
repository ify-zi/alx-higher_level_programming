#!/usr/bin/python3
def no_c(my_string):
    string_copy = []
    for i in my_string:
        if i != 'c' and i != 'C':
            string_copy.append(i)
    return ''.join(string_copy)
