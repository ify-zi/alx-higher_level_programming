#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if a_dictionary.get(key):
        a_dictionary[key] = value
    else:
        new_dict = {key: value}
        a_dictionary.update(new_dict)

    return a_dictionary
