import re


def valid_parentheses(string):
    parentheses_patern = r'[()]'
    find = re.findall(parentheses_patern, string)
    count = 0
    for item in find:
        if item == ')' and count == 0:
            return False
        elif item == ')':
            count -= 1
        elif item == '(':
            count += 1
    if count == 0:
        return True
    else:
        return False