def palindrome(string):
    string_reverse = string[::-1]
    if string == string_reverse:
        return True
    else:
        return False


string = input('Enter the string: ')

print(palindrome(string))
