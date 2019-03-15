# Task: Create the program which find simple numbers between 0 and customer number.


def is_prime(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    else:
        for number in range(2, num):
            if num % number == 0:
                return False
        else:
            return True


print(is_prime(2))
