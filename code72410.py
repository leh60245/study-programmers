""" 문제 설명
규칙
1. 아이디 길이 3 ~ 15
2. 소문자, 숫자, -, _, . 
3. "."는 처음과 끝에 사용 x, 그리고 연속으로 사용 x
"""


def solution(new_id):
    new_id = new_id.lower()

    filtered = []
    for c in new_id:
        if c.isalpha() or c.isdigit() or c in ("-", "_", "."):
            filtered.append(c)
    new_id = "".join(filtered)

    while ".." in new_id:
        new_id = new_id.replace("..", ".")

    new_id = new_id.strip(".")

    if new_id == "":
        new_id = "a"
    if len(new_id) > 15:
        new_id = new_id[:15]
    if new_id[-1] == ".":
        new_id = new_id[:-1]

    while len(new_id) < 3:
        new_id += new_id[-1]

    return new_id


print(solution("...!@BaT#*..y.abcdefghijklm"))

print(solution("z-+.^."))

print(solution("=.="))

print(solution("123_.def"))

print(solution("abcdefghijklmn.p"))
