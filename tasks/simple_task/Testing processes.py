def processes(start, end, processes):
    d = {}
    p = {}
    result = []
    for i in processes:
        d.update({i[1]: i[2]})
        p.update({i[1]: i[0]})
    try:
        n = start
        while n != end:
            result.append(p[n])
            n = d[n]
    except:
        result = []
    return result


test_processes = [
    ['gather', 'field', 'wheat'],
    ['bake', 'flour', 'bread'],
    ['mill', 'wheat', 'flour']
]
print(processes('field', 'bread', test_processes))
