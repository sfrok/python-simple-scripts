def find_short(s):
    content = s.split()
    short_word = len(sorted(content, key=len)[0])
    return short_word


print(find_short('dasdas dasda dsd sdsdadasd'))
