from itertools import combinations
from collections import defaultdict
from bisect import bisect_left as left_bound


def solution(info: list, query=None):
    answer = []
    people = defaultdict(list)

    for i in info:
        # 지원자 정보를 배열로 기록
        person = i.split()
        score = int(person.pop())
        people["".join(person)].append(score)

        # 지원자들의 조건으로 만들 수 있는 모든 조건을 키로 만듦
        # 미리 경우의 수를 만들어 두면 약간의 시간 비용을 소모하는 대신, 조회 비용을 비약적으로 줄일 수 있다.
        for j in range(4):
            case = list(combinations(person, j))
            for c in case:
                people["".join(c)].append(score)

    # 이진 탐색을 위해 만들어진 배열을 모두 오름차순으로 정렬한다.
    for i in people:
        people[i].sort()

    for i in query:
        key = i.split()
        score = int(key.pop())
        key = "".join(key)
        key = key.replace("and", "").replace(" ", "").replace("-", "")
        answer.append(len(people[key]) - left_bound(people[key], score))

    return answer


info = [  # 지원자 정보
    "java backend junior pizza 150",
    "python frontend senior chicken 210",
    "python frontend senior chicken 150",
    "cpp backend senior pizza 260",
    "java backend junior chicken 80",
    "python backend senior chicken 50",
]
query = [  # 지원 조건
    "java and backend and junior and pizza 100",
    "python and frontend and senior and chicken 200",
    "cpp and - and senior and pizza 250",
    "- and backend and senior and - 150",
    "- and - and - and chicken 100",
    "- and - and - and - 150",
]
print(solution(info, query))
