def make_negative( number ):
    check_number = str(number)
    if check_number[0] == '-':
        return number
    else:
        return number * (-1)


print(make_negative(-1))
