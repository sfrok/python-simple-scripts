'''
TO BE CONTINUED

import re


def encrypt_this(text):
    list_ascii_synbols = []  # get ascii smb for first letter in the words
    flag_for_get_first_letter = r"\b\w"
    get_first_letter = re.findall(flag_for_get_first_letter, text)
    for symbol in get_first_letter:
        list_ascii_synbols.append(ord(symbol))
    return list_ascii_synbols



print(encrypt_this("A wise old owl lived in an oak"))

'''