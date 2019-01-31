# Task: Create the program which find simple numbers between 0 and customer number.


customer_number = int(input('Enter natural number: '))
simple_numbers = []

for number in range(0, customer_number):
    if number > 1:
        for divider in range(2, number):
            if number % divider == 0:
                break
        else:
            simple_numbers.append(number)


print('Simple numbers: ', simple_numbers)
