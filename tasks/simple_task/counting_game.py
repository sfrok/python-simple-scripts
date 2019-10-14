def josephus(items, k):
    result = []
    element = 0
    score = 0
    while len(items) != 0:
        score += 1
        if score > k - 1:
            result.append(items.pop(element))
            score = 0
        else:
            element += 1
        if element >= len(items):
            element = 0
    return result


print(josephus([1, 2, 3, 4, 5, 6, 7], 3))
