def solution(answers):
    arr1 = [i for i in range(1, 6)]
    arr2 = [2, 1, 2, 3, 2, 4, 2, 5]
    arr3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt = [0, 0, 0]
    for i in range(len(answers)):
        if arr1[i] == answers[i]:
            cnt[0] += 1
        if arr2[i] == answers[i]:
            cnt[1] += 1
        if arr3[i] == answers[i]:
            cnt[2] += 1

    answer = []
    for idx, s in enumerate(cnt):
        if s == max(cnt):
            answers.append(idx + 1)

    return answer
