def collatz(n, answer):
    if answer >= 500:
        return -1
    if n == 1:
        return answer
    if n % 2 == 0:
        return collatz(n // 2, answer + 1)
    else:
        return collatz(n * 3 + 1, answer + 1)


def solution(n):
    return collatz(n, 0)


print(solution(6))
print(solution(16))
print(solution(626331))
