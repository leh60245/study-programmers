def solution(n, times):
    answer = 0
    # start로 최소한 걸릴 수 있는 시간을
    # end로 최대로 걸릴 수 있는 시간을 지정한다.
    # 책에서는 max(times) * n 로 지정했지만, 이런 최소 문제는 평균보다 아래이기에 평균으로 지정했다.
    start, end = 1, (sum(times) // len(times)) * n

    while start <= end:
        mid = (start + end) // 2
        people = 0
        test = []

        # 최대로 받을 수 있는 사람의 수를 계산한다.
        # 이때, 받을 수 있는 사람의 수가 주어진 고객수보다 크면 답으로 한다.
        # 보다 적다면, 더 많은 시간이 필요하므로 start를 증가시킨다.
        for time in times:
            people += mid // time
            if people >= n:
                break

        if people >= n:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1

    return answer


print(solution(1000, [7, 10, 3, 5, 100, 2000, 324, 123, 34]))
