def decomp(n):
    dict = {}
    for num in range(2, n+1):
        dict[num] = 0
        a = num
        for tmp in range(2, num+1):
            while a % tmp == 0:
                a /= tmp
                dict.update({tmp: dict[tmp]+1})
            if a == 1:
                break
    s = ''
    for num in range(2, n+1):
        if dict[num] > 0:
            s += str(num)
            if dict[num] > 1: s += '^' + str(dict[num])
            s += ' * '
    s = s[:len(s)-3]
    return s