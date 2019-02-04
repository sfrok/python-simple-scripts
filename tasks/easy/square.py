

import math


def square(side_square):
    p = 4 * side_square
    s = pow(side_square, 2)
    d = math.sqrt(2) * side_square
    result = (p, s, d)
    return result


side_square = int(input('Enter a side of square: '))

print(square(side_square))
