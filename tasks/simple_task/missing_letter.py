# need refactor


def find_missing_letter(chars):
    new_chars = []
    alphabet = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
    for smb in chars:
        new_chars.append(smb.upper())
    find_char = new_chars[0]
    index_find_char = alphabet.index(find_char)  # got index from alphabet
    cut_main_alphabet = alphabet[index_find_char:index_find_char + 26]  # got cut main alphabet
    for item in cut_main_alphabet:
        if item not in new_chars:
            if smb.islower():
                return item.lower()
            else:
                return item


print(find_missing_letter(['U', 'V', 'X', 'Y', 'Z']))
