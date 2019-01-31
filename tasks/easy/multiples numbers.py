# Task: Create the program which print all numbers multiples 5, between in two customer numbers.


first_num = int(input('Enter firs number: '))
second_num = int(input('Enter second number: '))
numbers = []

for number in range(first_num, second_num):
    if number % 5 == 0:
        numbers.append(number)


print(numbers)
