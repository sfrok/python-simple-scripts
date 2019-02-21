def unique_in_order(iterable):
    next_char = ''
    list = []
    for smb in iterable:
        if next_char != smb:
            list.append(smb)
            next_char = smb
    return list


print(unique_in_order('AAAAAAAAAABBBBBBBBDDDDDDD'))
