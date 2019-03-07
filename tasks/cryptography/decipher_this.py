import re


def decipher_this(string):
    var_patern = r'\d+'
    change_first_letter = []
    format_sentence = []
    text = string.split()
    find = re.findall(var_patern, string)
    for item_1, item_2 in zip(text, find):
        if item_2 in item_1:
            length = len(item_2)
            cut_number = item_1[0: length]
            cut_other_part = item_1[length:]
            change_first_letter.append(chr(int(cut_number)) + cut_other_part)
    for word in change_first_letter:
        length_word = len(word)
        if length_word <= 2:
            format_sentence.append(word)
        else:
            cut_first_letter = word[0]
            cut_second_letter = word[1]
            cut_last_letter = word[length_word - 1]
            cut_other_letter = word[2:length_word - 1]
            format_sentence.append(cut_first_letter + cut_last_letter + cut_other_letter + cut_second_letter)

    return ' '.join(format_sentence)


string = input('Enter a string which will decrypt: ')
print('Decrypted message: ', decipher_this(string))
