def bank(a, years):
    while years != 0:
        interim_amount = a * 0.1
        a += interim_amount
        years -= 1
    return a


a = int(input('Enter deposit amount: '))
years = int(input('Enter a term: '))

print(bank(a, years))
