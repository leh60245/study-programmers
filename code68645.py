def solution(n):
    arr = [[0] * i for i in range(1, n + 1)]
    x, y = -1, 0
    num = 1
    for i in range(n):
        for j in range(i, n):
            angle = i % 3
            if angle == 0:
                x += 1
            elif angle == 1:
                y += 1
            else:
                x -= 1
                y -= 1
            arr[x][y] = num
            num += 1
    return arr


print(solution(5))
