def iq_test(numbers):

    values = numbers.split(' ')
    check = []

    for num in values:
        if int(num) % 2 == 0:
            check.append(0)
        else:
            check.append(1)

    if sum(check) == 1:
        return check.index(1) + 1
    else:
        return check.index(0) + 1


print(iq_test('1 2 1 1'))
