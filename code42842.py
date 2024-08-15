import math


def solution(brown, yellow):
    tmp = int(math.pow(yellow, 1 / 2))
    for i in range(1, tmp + 1):
        if yellow % i == 0:
            share = yellow // i
            if (share + i) * 2 + 4 == brown:
                return [share + 2, i + 2]


print(solution(10, 2))

print(solution(8, 1))

print(solution(24, 24))
