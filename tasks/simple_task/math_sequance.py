import math

x = float(input('Enter the x: '))
k = score = 0
c = sum_value = ((-1) ** k) * x ** (2 * k + 1) / math.factorial(2 * k + 1)
c_n = c + 1
eps = 10 ** (-3)

while abs(c - c_n) > eps:
    k += 1
    c_n = c
    c = ((-1) ** k) * x ** (2 * k + 1) / math.factorial(2 * k + 1)
    score += 1
    sum_value += c
print(f'amount of score {score}, sum value {sum_value}, '
      f'sin(x)={math.sin(x)}')
