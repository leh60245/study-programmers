"""
코드 작성
1. 제재 아이디 규칙을 정규표현식에 맞게 수정한다.
2. DFS와 비트마스킹을 사용해 유저 아이디와 제재 아이디 규칙을 검사한다.
이번 DFS는 재귀 함수를 사용해 개발할 것이므로 -> 시작 조건, 종료 조건, 점화식이 필요하다.
    시작 조건은 1번 과정에서 주어진 아이디에서 가장 첫 아이디를 검사하는 것이다.
    점화식은 "다음 제재 아이디"와 "다음 방문 상태"를 점검하여 규칙이 서로 일치하는지 확인하는 과정이다.
    종료 조건은 마지막 제재 아이디에 도달했을 때를 기준으로 한다.
이 과정 중 '각 단어를 제한 규칙에 하나씩 비교하는' 모양이 나온다.
여기서 비트마스킹을 사용해 추가적으로 최정화할 수 있다.
각 단어별로 2진수 고유 번호를 지정해준 다음, -> 제재 아이디 규칙과 계산하여 -> 체크한 부분을 1, 그렇지 않은 부분을 0으로 표현하면
-> 변수 하나로 현재 진행 상태를 갖도록 만들 수 있다.
"""

import re


def search(ban_idx: int, visit: int, userId: list, answer: set, banPatterns: list):
    # user에게 이진수로 표현된 고유 번호를 매긴다. 1, 10, 100, 1000, ...
    # visit은 이진수로 표현된 user id를 저장하는 변수로,
    # 저장하는 방법은 visit | (1 << user_idx) 이다.
    # 방문한 적이 없고, 제재 아이디와 동일하다면, 위 방식으로 저장되면서 다음 함수를 호출하는 것이다.
    # 방문한 적이 있는 user을 확인하는 방법은 visit & (1 << user_idx) 이다.
    if ban_idx == len(banPatterns):
        answer.add(visit)
        return
    for user_idx in range(len(userId)):
        # 검색할 문자가 이미 확인한 상태이거나,
        # 한 번이라도 규칙을 통과하지 못하면(제제 아이디와 다르다면)
        # 해당 아이디는 조사할 필요가 없으므로 함수 호출을 막는다
        # -> 백트래킹 기법
        if (visit & (1 << user_idx)) > 0 or not re.fullmatch(
            banPatterns[ban_idx], userId[user_idx]
        ):
            continue
        print(banPatterns[ban_idx], userId[user_idx])
        search(ban_idx + 1, visit | (1 << user_idx), userId, answer, banPatterns)


def solution(userId: list, bannedId: list) -> int:
    answer = set()  # 정답을 기록할 변수
    banPatterns = [
        x.replace("*", ".") for x in bannedId
    ]  # 제재 아이디 규칙을 리스트 컴프리헨션 방식으로 정규표현식에 적합하게 변환
    search(0, 0, userId, answer, banPatterns)  # 모든 경우의 수를 조사할 함수
    return len(answer)


user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["*rodo", "*rodo", "******"]
print(solution(user_id, banned_id))
