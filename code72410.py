""" 문제 설명
규칙
1. 아이디 길이 3 ~ 15
2. 소문자, 숫자, -, _, . 
3. "."는 처음과 끝에 사용 x, 그리고 연속으로 사용 x
"""


def solution(new_id):
    # 1. 소문자 치환
    new_id = new_id.lower()

    # 2. 사용 가능한 문자를 제외한 모든 문자 제거
    available_characters = (
        [chr(i) for i in range(ord("a"), ord("z") + 1)]
        + [str(i) for i in range(10)]
        + ["-", "_", "."]
    )
    tmp = []
    for i in new_id:
        if i in available_characters:
            if i == "." and (tmp == [] or tmp[-1] == "."):
                continue
            tmp.append(i)
    if tmp != [] and tmp[-1] == ".":
        tmp = tmp[:-1]
    new_id = "".join(tmp)

    # 5, 6
    if new_id == "":
        new_id = "a"
    if len(new_id) > 15:
        new_id = new_id[:15]
        if new_id[-1] == ".":
            new_id = new_id[:-1]
    if len(new_id) <= 2:
        new_id = new_id + (new_id[-1] * (3 - len(new_id)))

    return new_id


print(solution("...!@BaT#*..y.abcdefghijklm"))

print(solution("z-+.^."))

print(solution("=.="))

print(solution("123_.def"))

print(solution("abcdefghijklmn.p"))
