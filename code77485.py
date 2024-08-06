# 3. 행렬을 시계 방향으로 회전시키기
def rotate(x1, y1, x2, y2, matrix):
    first = matrix[x1][y1]  # 맨 첫 번째 숫자만 기억해두기
    min_value = first  # 첫 번째 숫자가 곧 문제의 답이 될 수 있으므로, 따로 저장하기

    # 왼쪽
    for k in range(x1, x2):
        matrix[k][y1] = matrix[k + 1][y1]
        min_value = min(matrix[k][y1], min_value)
    # 아래
    for k in range(y1, y2):
        matrix[x2][k] = matrix[x2][k + 1]
        min_value = min(matrix[x2][k], min_value)
    # 오른쪽
    for k in range(x2, x1, -1):
        matrix[k][y2] = matrix[k - 1][y2]
        min_value = min(matrix[k][y2], min_value)
    # 위
    for k in range(y2, y1 + 1, -1):
        matrix[x1][k] = matrix[x1][k - 1]
        min_value = min(matrix[x1][k], min_value)
    # 첫 번째 값
    matrix[x1][y1 + 1] = first
    return min_value


def solution(rows, columns, queries):
    # 1. 행렬 만들기
    matrix = [
        [(row) * columns + (col + 1) for col in range(columns)] for row in range(rows)
    ]

    # 2. 회전해야 할 위치들의 값을 받아오기
    result = []
    for x1, y1, x2, y2 in queries:
        result.append(rotate(x1 - 1, y1 - 1, x2 - 1, y2 - 1, matrix))
    return result


if __name__ == "__main__":
    rows, columns, queries = 6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]
    print(solution(rows, columns, queries))
