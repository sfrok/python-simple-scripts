def xo(s):
    if s.lower().count('x') == s.lower().count('o'):
        return True
    else:
        return False


print(xo('xo'))