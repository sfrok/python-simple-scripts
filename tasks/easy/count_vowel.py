def getCount(inputStr):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = 0
    for vowel in vowels:
        result += inputStr.count(vowel)
    return result


print(getCount(inputStr='ooabcuii'))
