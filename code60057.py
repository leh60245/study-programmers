"""
문제 풀이 흐름
1. 압축은 "동일한 단어가 문자열 내에 존재할 때 가능"하다. 압축이 가능한 최대 단어 길이는 주어진 단어의 1/2
2. 해당 규칙이 몇 번 반복되었는지 확인하기 위해 이를 관리하는 변수가 필요하다. 반복된 횟수가 2번 이상일 때만 숫자를 붙여 반환한다.
3. 주어진 규칙을 바탕으로 전체를 조사해야 한다.
3-1. 현재 자기 위치의 단어와 현재 규칙만큼 앞의 위치를 확인하며 진행해야 한다.
3-2. 주어진 규칙의 길이보다 남은 길이가 짧다면 찾을 수 없기 때문에, 탐색을 중단하거나 미리 탐색 범위를 조정해야 한다.
4. 최종적으로 "줄인 문자열"과 "원래 문자열"의 길이 중 누가 짧은지 비교한다.

그 외 고민사항
Q. 압축된 코드를 가지고 있어야 하는가?
A. 필요 없다. b/c 압축된 문자열이 중요한 게 아니라, 압축된 문자열의 '길이'가 중요하다. 

풀이방법 2. 문자열에서 가능한 모든 규칙을 뽑아내서 비교하기
1. 압축 가능한 길이만큼 순회하기
2. 전체 문자열에서 가능한 모든 규칙을 먼저 생성하기
3. 만든 규칙을 전부 비교 검사하기
4. 압축 과정에서 나온 문자열의 길이와 원래 문자열의 길이 비교하기
"""


def compress(s, length):
    # 전체 문자열에서 가능한 모든 규칙 생성
    words = [s[i : i + length] for i in range(0, len(s), length)]

    # 만든 규칙을 전부 비교 검사
    res = []  # 압축된 단어와 반복 횟수를 저장하는 배열
    cur_word = words[0]  # 첫 번째 단어 저장
    cur_cnt = 1
    for pattern, compare in zip(words, words[1:] + [""]):
        if pattern == compare:
            cur_cnt += 1
            continue
        res.append([cur_word, cur_cnt])
        cur_word = compare
        cur_cnt = 1

    # 압축 과정에서 나온 문자열의 길이와 원래 문자열의 길이 비교
    ### 배워갈 점: if else 구문을 ()로 묶어 범위를 지정할 수 있다. ###
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)


def solution(s):
    if len(s) == 1:
        return 1
    return min(compress(s, length) for length in list(range(1, len(s) // 2 + 1)))


print(solution("aabbaccc"))

print(solution("ababcdcdababcdcd"))

print(solution("abcabcdede"))

print(solution("abcabcabcabcdededededede"))

print(solution("xababcdcdababcdcd"))
