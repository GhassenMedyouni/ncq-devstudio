"""
Author : Medyouni Ghassen
"""

##  ALGO  1

def solution_1(N, A):
    result = [0] * (N + 1)
    max_to_set = 0
    max_counter = 0
    for x in A:
        if 1 <= x <= N:

            if result[x] < max_to_set:
                result[x] = max_to_set

            result[x] += 1

            if max_counter < result[x]:
                max_counter = result[x]

        else:
            max_to_set = max_counter

    result = result[1:]
    return [max(max_to_set, i) for i in result]

N = 5
A = [3, 4, 4, 6, 1, 4, 4]
print(solution_1(N, A))
