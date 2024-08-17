from itertools import combinations


def solution(numbers: list):
    return sorted(set(map(sum, combinations(numbers, 2))))


print(solution([2, 1, 3, 4, 1]))
