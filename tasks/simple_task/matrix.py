"""
Pascal's triangle
"""


n = int(input('N: '))
matrix = [[] for i in range(n)]

for row in range(len(matrix)):
    for elem in range(row+1):
        if elem == 0 or elem == row:
            matrix[row].append(1)
        else:
            matrix[row].append(matrix[row-1][elem] + matrix[row-1][elem-1])

for row in matrix:
    print("")
    for elem in row:
        print(elem, end=" ")
