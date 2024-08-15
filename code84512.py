# 사전을 기록할 배열, 현재 문자열, 현재 문자열 숫자
def find(data, p, step) -> None:
    # 종료 조건 명시: 최대 5글자까지만 가능하도록 함
    if step == 6:
        return
    # 사전(data)에 추가
    if p != "":
        data.append(p)
    # 문자열을 모음 순서대로 합쳐서 다음 재귀 호출
    for c in ["A", "E", "I", "O", "U"]:
        find(data, "".join([p, c]), step + 1)


def solution(word):
    answer = 0
    data = []
    find(data, "", 0)
    for i in range(len(data)):
        if data[i] == word:
            answer = i + 1
            break

    return answer
