# Task: make simple operations with numbers.


first_num = int(input('Enter firs number: '))
second_num = int(input('Enter second number: '))
sign = input("Enter sign '+' or '-': ")

if sign == '-':
    print('Result is: ', first_num - second_num)
elif sign == '+':
    print('Result is: ', first_num + second_num)
else:
    print('Error')

