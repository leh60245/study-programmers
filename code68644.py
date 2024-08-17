from itertools import combinations


def solution(numbers: list):
    arr = set()  # 숫자 중복을 방지하기 위한 set 지정
    selects = list(combinations(numbers, 2))  # 순열로 2개 선택
    for select in selects:
        (a, b) = select
        arr.add(a + b)
    return sorted(arr)


print(solution([2, 1, 3, 4, 1]))
