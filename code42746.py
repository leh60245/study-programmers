from functools import cmp_to_key


def solution(numbers):
    numbers = [str(x) for x in numbers]
    numbers.sort(key=lambda x: x * 3, reverse=True)
    result = "".join(numbers)
    if "0" * len(numbers) == result:
        return "0"
    return result


print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
