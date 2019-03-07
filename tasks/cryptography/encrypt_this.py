def encrypt_this(text):
    start_text = text.split()
    change_letter = []  # change place of letters
    format_words = []  # get mass of crypt each word

    for char in start_text:
        length_char = len(char)
        if length_char <= 2:
            change_letter.append(char)
        else:
            cut_first_letter = char[0]
            cut_second_letter = char[1]
            cut_some_letter = char[2:length_char - 1]
            cut_last_letter = char[length_char - 1]
            change_letter.append(cut_first_letter + cut_last_letter +
                                 cut_some_letter + cut_second_letter)
    for word in change_letter:
        cut_first_letter_change = word[0]
        cut_other_part = word[1:]
        format_words.append(str(ord(cut_first_letter_change)) + cut_other_part)

    return ' '.join(format_words)


text = input('Enter a string which will be encrypt: ')
print('Encrypted string: ', encrypt_this(text))
