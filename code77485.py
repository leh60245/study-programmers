def solution(rows, columns, queries):
    # 1. 행렬 만들기
    board = [
        [(row) * columns + (col + 1) for col in range(columns)] for row in range(rows)
    ]

    # 2. 회전해야 할 위치들의 값을 받아오기
    result = []
    for query in queries:
        a, b, c, d = query[0] - 1, query[1] - 1, query[2] - 1, query[3] - 1
        row1, row2 = board[a][b:d], board[c][b + 1 : d + 1]
        _min = min(row1 + row2)

        for i in range(c, a, -1):
            board[i][d] = board[i - 1][d]
            _min = min(_min, board[i][d])

        for i in range(a, c):
            board[i][b] = board[i + 1][b]
            _min = min(_min, board[i][b])

        board[a][b + 1 : d + 1], board[c][b:d] = row1, row2
        result.append(_min)

    return result


if __name__ == "__main__":
    rows, columns, queries = 6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]
    print(solution(rows, columns, queries))
