def series_sum(n):
    result = 0
    for i in range(n):
        result += 1 / (1 + i * 3)
    return '{:.2f}'.format(result)


print(series_sum(0))
