def find_short(s):
    list = s.split()
    l = len(sorted(list, key = len)[0])
    return l


print(find_short('dasdas dasda dsd sdsdadasd'))