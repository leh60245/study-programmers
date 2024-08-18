from functools import cmp_to_key


def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=cmp_to_key(lambda x, y: int(x + y) - int(y + x)), reverse=True)
    return str(int("".join(numbers)))


print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
