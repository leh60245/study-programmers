def solution(line):
    meet = list()
    # n = len(line)

    x_min = y_min = int(1e15)
    x_max = y_max = -int(1e15)
    # 주어진 직선에서 교점 구하기
    # 시간 복잡도 O(n^2)보다 조금 더 빠름
    for i in range(len(line)):
        a, b, e = line[i]
        for j in range(i + 1, len(line)):
            c, d, f = line[j]
            if (a * b) - (b * c) == 0:  # (2) 뺄셈하여 0과 비교로 변경
                continue
            x = ((b * f) - (e * d)) / ((a * d) - (b * c)) # 괄호를 추가하여 계신 실수 방지
            y = ((e * c) - (a * f)) / ((a * d) - (b * c))

            # 정수 교점만 저장
            if x.is_integer() and y.is_integer():
                x = int(x)
                y = int(y)
                meet.append([x, y])
                # 교점을 모두 모은 상태에서 할 때, 추가 비용이 발생하므로, 교점을 계산했을 때마다 수치를 확인
                x_max, y_max = max(x_max, x), max(y_max, y)
                x_min, y_min = min(x_min, x), min(y_min, y)

    width = abs(x_max - x_min) + 1
    height = abs(y_max - y_min) + 1
    answer = [["."] * width for _ in range(height)]
    meet = sorted(meet, key = lambda i: -i[1])

    for x, y in meet:
        ny = y_max - y
        nx = x - x_min
        answer[ny][nx] = "*"

    return list(map(''.join, answer))
