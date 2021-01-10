"""
Author : Medyouni Ghassen
"""


###  ALGO 3
def solution_3(A):
    N = len(A)
    M = 0

    for i in range(N):
        A[i] = abs(A[i])
        M = max(A[i], M)

    S = sum(A)
    count = [0] * (M + 1)

    for i in range(N):
        count[A[i]] += 1

    V = [-1] * (S + 1)
    V[0] = 0

    for a in range(1, M + 1):
        if count[a] > 0:
            for j in range(S):
                if V[j] >= 0:
                    V[j] = count[a]
                elif (j >= a and V[j - a] > 0):
                    V[j] = V[j - a] - 1

    result = S

    for i in range(S // 2 + 1):
        if V[i] >= 0:
            result = min(result, S - 2 * i)
    return result

# test 1
A = [1, 5, 2, -2]
print(solution_3(A))

# test 2
A = []
print(solution_3(A))

# test 3
A = [7, 1]
print(solution_3(A))
