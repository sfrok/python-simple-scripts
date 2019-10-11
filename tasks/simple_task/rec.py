"""
Cn = 3*C(n-1)+C(n-2);
C1 = 1;
C2 = 2;
"""


def recursion_depth(number):
    if number == 1:
        return 1
    elif number == 2:
        return 2
    elif number > 2:
        return 3 * recursion_depth(number - 1) + recursion_depth(number - 2)
    else:
        return 'Enter a "number" > 0'


number = int(input("Enter the 'n': "))
print(recursion_depth(number))


"""
def matrix(a, d, N):
    mat = [[] for i in range(N)]
    score = 0
    for str in range(N):
        while len(mat[str]) < N:
            mat[str].append(a+d*score)
            score += 1
    return mat


a = int(input('Enter the value of first element: '))
d = int(input('Enter the step: '))
N = int(input('Enter the matrix size: '))
print(matrix(a, d, N))
"""

"""
Cn = C(n/3) + 2
C1 = 1



def recursion_depth(n):
    if n == 1:
        return 1
    elif n % 3 == 0 and type(lr2(n/3)) == int:
        return recursion_depth(n/3) + 2
    else:
        return "Wrong number!"
"""

"""
def matrix(a, d, n):
    l = [a + d * i for i in range(n * n)]
    return [l[i:i + n] for i in range(0, len(l), n)]


print(matrix(int(input("a: ")), int(input("d: ")), int(input("n: "))))
"""