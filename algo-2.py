"""
Author : Medyouni Ghassen
"""

####   ALGO 2

def solution_2(A, B):
    max_num = max(A)
    N = len(A)
    K = [0, 1] + [-1] * max_num
    result = [0] * N

    for x in range(2, max_num + 2):
        K[x] = K[x - 2] + K[x - 1]

    K = K[2:]

    for x in range(N):
        value = K[A[x] - 1]
        result[x] = value & ((1 << B[x]) - 1)

    return result

A = [4, 4, 5, 5, 1]
B = [3, 2, 4, 3, 1]
print(solution_2(A, B))
