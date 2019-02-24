# option 1

def bank(a, years):
    while years != 0:
        interim_amount = a * 0.1
        a += interim_amount
        years -= 1
    return a


a = int(input('Enter deposit amount: '))
years = int(input('Enter a term: '))

print(bank(a, years))


# option2

def bank(a, years):
    if years > 0:
        return bank(a + a / 10, years - 1)
    print(a)


a = int(input('Enter deposit amount: '))
years = int(input('Enter a term: '))

bank(a, years)
