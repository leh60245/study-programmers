arr = [1, 2, 3, 4]
# 순서를 고려하기 위한 배열
visited = [0] * len(arr)


def permutations(n, new_arr):
    if len(new_arr) == n:
        print(new_arr)
        return

    for i in range(len(arr)):
        if not visited[i]:
            visited[i] = 1
            permutations(n, new_arr + [arr[i]])
            visited[i] = 0


permutations(2, [])
